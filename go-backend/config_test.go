package main

import (
	"testing"
	"text/template"

	"github.com/google/go-cmp/cmp"
	"github.com/google/go-cmp/cmp/cmpopts"
)

func Test_configFromEnv(t *testing.T) {
	t.Setenv("LISTEN_HOST", "127.0.0.1")
	t.Setenv("LISTEN_PORT", "8080")
	t.Setenv("AKISMET_ENABLED", "TRUE")
	t.Setenv("AKISMET_KEY", "akismet-key")
	t.Setenv("DB_HOST", "127.0.0.1")
	t.Setenv("DB_PORT", "5432")
	t.Setenv("DB_DB", "test")
	t.Setenv("DB_USER", "postgres")
	t.Setenv("DB_PASS", "postgres-pass")
	t.Setenv("MAIL_ENABLED", "TRUE")
	t.Setenv("SMTP_SERVER", "localhost")
	t.Setenv("SMTP_PORT", "25")
	t.Setenv("SMTP_USER", "mailuser")
	t.Setenv("SMTP_PASS", "mailpass")
	t.Setenv("MAIL_TO", "receiver@example.com")
	t.Setenv("MAIL_FROM", "sender@example.com")
	t.Setenv("MAIL_BODY_NEW_COMMENT", "new comment: {{ .content }}")
	t.Setenv("COMMENT_TAG_WHITELIST", "b,i,a")
	t.Setenv("COMMENT_ATTRIBUTE_WHITELIST", `{"a":["href"]}`)
	want := Config{
		ListenHost: "127.0.0.1",
		ListenPort: 8080,
		AkismetKey: "akismet-key",
		DB: DBConfig{
			Host:     "127.0.0.1",
			Port:     5432,
			DB:       "test",
			User:     "postgres",
			Password: "postgres-pass",
		},
		Mail: &MailConfig{
			Server:                 "localhost",
			Port:                   25,
			User:                   "mailuser",
			Password:               "mailpass",
			To:                     "receiver@example.com",
			From:                   "sender@example.com",
			NewCommentBodyTemplate: nil, // ignored
		},
		CommentTagWhitelist: Set[string]{
			"b": struct{}{},
			"i": struct{}{},
			"a": struct{}{},
		},
		CommentAttributeWhitelist: map[string]Set[string]{
			"a": {
				"href": struct{}{},
			},
		},
	}
	got, err := configFromEnv()
	if err != nil {
		// We're only testing the happy path.
		// Hey, at least I have tests at all.
		t.Fatal(err)
	}
	if diff := cmp.Diff(got, &want, cmpopts.IgnoreTypes((*template.Template)(nil))); diff != "" {
		t.Error(diff)
	}
}
