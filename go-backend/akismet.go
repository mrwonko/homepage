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

func commentToAkismet(comment *dbComment) url.Values {
	res := url.Values{
		"blog":                 []string{"http://mrwonko.de/blog"},
		"blog_lang":            []string{"en"},
		"blog_charset":         []string{"UTF-8"},
		"comment_type":         []string{"comment"},
		"comment_author":       []string{comment.Author},
		"comment_author_email": []string{comment.Email},
		"user_agent":           []string{comment.UserAgent},
		"user_ip":              []string{comment.IP},
	}
	if comment.URL.Valid {
		res.Set("comment_author_url", comment.URL.String)
	}
	if comment.Referrer.Valid {
		res.Set("referrer", comment.Referrer.String)
	}
	if comment.UnsanitizedContent.Valid {
		res.Set("comment_content", comment.UnsanitizedContent.String)
	} else {
		res.Set("comment_content", comment.Content)
	}
	return res
}

func (a *Akismet) Check(ctx context.Context, comment *dbComment) (spammy Spamminess, err error) {
	const akismetTimeout = 5 * time.Second
	ctx, cancel := context.WithTimeout(ctx, akismetTimeout)
	defer cancel()
	body := commentToAkismet(comment)
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
	if !(200 <= resp.StatusCode && resp.StatusCode < 300) {
		return Ham, fmt.Errorf("status code %d, body: %s", resp.StatusCode, respBody)
	}
	if err != nil {
		return Ham, fmt.Errorf("reading response %d body: %w", resp.StatusCode, err)
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

func (a *Akismet) SubmitHam(ctx context.Context, comment *dbComment) error {
	const akismetTimeout = 5 * time.Second
	ctx, cancel := context.WithTimeout(ctx, akismetTimeout)
	defer cancel()
	body := commentToAkismet(comment)
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, fmt.Sprintf("https://%s.rest.akismet.com/1.1/submit-ham", string(a.APIKey)), strings.NewReader(body.Encode()))
	if err != nil {
		return fmt.Errorf("creating request: %w", err)
	}
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return fmt.Errorf("posting request: %w", err)
	}
	respBody, err := io.ReadAll(resp.Body)
	err = cmp.Or(err, resp.Body.Close())
	if err != nil {
		return fmt.Errorf("reading response %d body: %w", resp.StatusCode, err)
	}
	if !(200 <= resp.StatusCode && resp.StatusCode < 300) {
		return fmt.Errorf("status code %d, body: %s", resp.StatusCode, respBody)
	}
	return nil
}

func (a *Akismet) SubmitSpam(ctx context.Context, comment *dbComment) error {
	const akismetTimeout = 5 * time.Second
	ctx, cancel := context.WithTimeout(ctx, akismetTimeout)
	defer cancel()
	body := commentToAkismet(comment)
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, fmt.Sprintf("https://%s.rest.akismet.com/1.1/submit-spam", string(a.APIKey)), strings.NewReader(body.Encode()))
	if err != nil {
		return fmt.Errorf("creating request: %w", err)
	}
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return fmt.Errorf("posting request: %w", err)
	}
	respBody, err := io.ReadAll(resp.Body)
	err = cmp.Or(err, resp.Body.Close())
	if err != nil {
		return fmt.Errorf("reading response %d body: %w", resp.StatusCode, err)
	}
	if !(200 <= resp.StatusCode && resp.StatusCode < 300) {
		return fmt.Errorf("status code %d, body: %s", resp.StatusCode, respBody)
	}
	return nil
}
