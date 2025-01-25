package main

import (
	"bytes"
	"context"
	"fmt"
	"net/smtp"
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
	err = smtp.SendMail(addr, nil, m.config.From, []string{m.config.To}, body.Bytes())
	if err != nil {
		return fmt.Errorf("sending email: %w", err)
	}
	return nil
}
