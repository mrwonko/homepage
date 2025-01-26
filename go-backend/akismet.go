package main

import (
	"cmp"
	"context"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
	"time"
)

type Akismet struct {
	APIKey Secret
}

type Spamminess int

const (
	Ham Spamminess = iota
	Spam
	Discard
)

func (a *Akismet) Check(ctx context.Context, comment *dbComment) (spammy Spamminess, err error) {
	const akismetTimeout = 5 * time.Second
	ctx, cancel := context.WithTimeout(ctx, akismetTimeout)
	defer cancel()
	body := url.Values{
		"blog":                 []string{"http://mrwonko.de/blog"},
		"blog_lang":            []string{"en"},
		"blog_charset":         []string{"UTF-8"},
		"comment_type":         []string{"comment"},
		"comment_author":       []string{comment.Author},
		"comment_author_email": []string{comment.Email},
		"comment_content":      []string{comment.UnsanitizedContent},
		"user_agent":           []string{comment.UserAgent},
		"referrer":             []string{comment.Referrer},
		"user_ip":              []string{comment.IP},
	}
	if comment.URL.Valid {
		body.Set("comment_author_url", comment.URL.String)
	}
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, fmt.Sprintf("https://%s.rest.akismet.com/1.1/comment-check", string(a.APIKey)), strings.NewReader(body.Encode()))
	if err != nil {
		return Ham, fmt.Errorf("creating request: %w", err)
	}
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return Ham, fmt.Errorf("posting request: %w", err)
	}
	respBody, err := io.ReadAll(resp.Body)
	err = cmp.Or(err, resp.Body.Close())
	if 200 > resp.StatusCode || resp.StatusCode >= 300 {
		return Ham, fmt.Errorf("status code %d, body: %s", resp.StatusCode, respBody)
	}
	switch strings.TrimSpace(string(respBody)) {
	case "true":
		if resp.Header.Get("X-akismet-pro-tip") == "discard" {
			return Discard, nil
		}
		return Spam, nil
	case "false":
		return Ham, nil
	default:
		return Ham, fmt.Errorf("unexpected response: %s", respBody)
	}
}
