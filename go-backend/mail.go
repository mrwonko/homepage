package main

import (
	"bytes"
	"context"
	"crypto/tls"
	"errors"
	"fmt"
	"net/smtp"
	"slices"
	"strings"
)

type Mailer struct {
	config *MailConfig
}

/*

de/blog/{{.post}}.html\">{{.post}}</a>, it's probably {{.spammy}}.</p>
<p>
    author: {{.author}}<br/>
    email: {{.email}}<br/>
    url: {{.url}}<br/>
    Content:
{{.content}}
*/

var mailContentReplacer = strings.NewReplacer("<", "&lt;", ">", "&gt;", "\n", "<br/>\r\n")

func (m *Mailer) SendCommentNotification(ctx context.Context, year int, articleSlug string, comment *dbComment) error {
	var body bytes.Buffer
	fmt.Fprintf(&body, "From: %s\n", m.config.From)
	fmt.Fprintf(&body, "To: %s\n", m.config.To)
	fmt.Fprintf(&body, "Subject: New blog comment on %d/%s\n", year, articleSlug)
	fmt.Fprintln(&body, "Content-Type: text/html; charset=\"utf-8\"")
	body.WriteString("\n\n") // (empty) headers + empty line
	spammy := "spam"
	if !comment.Spam {
		spammy = "ham"
	}
	err := m.config.NewCommentBodyTemplate.Execute(&body, map[string]string{
		"post":    fmt.Sprintf("%d/%s", year, articleSlug),
		"spammy":  spammy,
		"author":  comment.Author,
		"email":   comment.Email,
		"url":     comment.URL.String,
		"content": mailContentReplacer.Replace(comment.UnsanitizedContent),
	})
	if err != nil {
		return fmt.Errorf("executing mail body template: %w", err)
	}
	addr := fmt.Sprintf("%s:%d", m.config.Server, m.config.Port)
	client, err := smtp.Dial(addr)
	if err != nil {
		return fmt.Errorf("dialing smtp server: %w", err)
	}
	defer client.Close()
	if err := client.Hello("localhost"); err != nil {
		return fmt.Errorf("SMTP HELO: %w", err)
	}
	if ok, _ := client.Extension("STARTTLS"); ok {
		config := &tls.Config{ServerName: m.config.CertHostname}
		if err = client.StartTLS(config); err != nil {
			return fmt.Errorf("StartTLS: %w", err)
		}
	}
	var auths Set[string]
	if ok, authString := client.Extension("AUTH"); !ok {
		return errors.New("smtp: server doesn't support AUTH")
	} else {
		auths = SetOf(slices.Values(strings.Split(authString, " ")))
	}
	var auth smtp.Auth
	switch {
	case auths.Contains("PLAIN"):
		auth = smtp.PlainAuth("", string(m.config.User), string(m.config.Password), m.config.Server)
	case auths.Contains("LOGIN"):
		auth = SMTPLoginAuth("", string(m.config.User), string(m.config.Password), m.config.Server)
	default:
		return fmt.Errorf("server neither supports LOGIN nor PLAIN auth, only %#v", auths)
	}
	if err := client.Auth(auth); err != nil {
		return fmt.Errorf("smtp auth: %w", err)
	}
	if err := client.Mail(m.config.From); err != nil {
		return fmt.Errorf("smtp mail: %w", err)
	}
	if err := client.Rcpt(m.config.To); err != nil {
		return fmt.Errorf("smtp rcpt: %w", err)
	}
	w, err := client.Data()
	if err != nil {
		return fmt.Errorf("smtp data: %w", err)
	}
	_, err = w.Write(body.Bytes())
	if err != nil {
		return fmt.Errorf("smtp write: %w", err)
	}
	err = w.Close()
	if err != nil {
		return fmt.Errorf("smtp close: %w", err)
	}
	err = client.Quit()
	if err != nil {
		return fmt.Errorf("smtp quit: %w", err)
	}
	return nil
}

// Implementation of the deprecated SASL "LOGIN" mechanism for SMTP,
// as specified in https://www.ietf.org/archive/id/draft-murchison-sasl-login-00.txt
type smtpLoginAuth struct {
	identity, username, password string
	host                         string
}

func SMTPLoginAuth(identity, username, password, host string) smtp.Auth {
	return &smtpLoginAuth{
		identity: identity,
		username: username,
		password: password,
		host:     host,
	}
}

func (s *smtpLoginAuth) Start(server *smtp.ServerInfo) (string, []byte, error) {
	if !server.TLS && server.Name != "localhost" && server.Name != "127.0.0.1" && server.Name != "::1" {
		return "", nil, errors.New("unencrypted connection")
	}
	if server.Name != s.host {
		return "", nil, errors.New("wrong host name")
	}
	// the initial message only contains the mechanism,
	// the server then sends challenges for username and password (see Next())
	return "LOGIN", nil, nil
}

func (s *smtpLoginAuth) Next(fromServer []byte, more bool) ([]byte, error) {
	if more {
		switch string(fromServer) {
		case "Username", "Username:":
			return []byte(s.username), nil
		case "Password", "Password:":
			return []byte(s.password), nil
		default:
			return nil, fmt.Errorf("unexpected server challenge %q", fromServer)
		}
	}
	return nil, nil
}
