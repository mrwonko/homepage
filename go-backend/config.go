package main

import (
	"bytes"
	"cmp"
	"encoding/json"
	"errors"
	"fmt"
	"iter"
	"maps"
	"os"
	"slices"
	"strconv"
	"strings"
	"text/template"
)

type Config struct {
	ListenHost string
	ListenPort uint16

	AkismetKey Secret

	DB DBConfig

	Mail *MailConfig

	CommentTagWhitelist       Set[string]
	CommentAttributeWhitelist map[string]Set[string]
}

type Set[Elem cmp.Ordered] map[Elem]struct{}

func SetOf[Elem cmp.Ordered](elems iter.Seq[Elem]) Set[Elem] {
	res := Set[Elem]{}
	for elem := range elems {
		res[elem] = struct{}{}
	}
	return res
}

func (s Set[Elem]) Contains(elem Elem) bool {
	_, ok := s[elem]
	return ok
}

func (s Set[Elem]) GoString() string {
	if s == nil {
		return "nil"
	}
	var res bytes.Buffer
	_, _ = res.WriteRune('{')
	for i, elem := range slices.Sorted(maps.Keys(s)) {
		if i > 0 {
			_, _ = res.WriteString(", ")
		}
		fmt.Fprintf(&res, "%#v", elem)
	}
	_, _ = res.WriteRune('}')
	return res.String()
}

func (cfg *Config) AkismetEnabled() bool {
	return cfg.AkismetKey != ""
}

func (cfg *Config) SMTPEnabled() bool {
	return cfg.Mail != nil
}

type DBConfig struct {
	Host     string
	Port     uint16
	DB       string
	User     Secret
	Password Secret
}

type MailConfig struct {
	Server                 string
	Port                   uint16
	CertHostname           string
	User                   Secret
	Password               Secret
	To                     string
	From                   string
	NewCommentBodyTemplate *template.Template
}

type Secret string

func (s Secret) GoString() string {
	return "<redacted>"
}

func configFromEnv() (*Config, error) {
	var res Config

	errs := []error{
		readEnvString("LISTEN_HOST", &res.ListenHost),
		readEnvUint16("LISTEN_PORT", &res.ListenPort),
	}
	var akismetEnabled bool
	if err := readEnvBool("AKISMET_ENABLED", &akismetEnabled); err != nil {
		errs = append(errs, err)
	} else if akismetEnabled {
		errs = append(errs, readEnvSecret("AKISMET_KEY", &res.AkismetKey))
	}
	errs = append(errs,
		readEnvString("DB_HOST", &res.DB.Host),
		readEnvUint16("DB_PORT", &res.DB.Port),
		readEnvString("DB_DB", &res.DB.DB),
		readEnvSecret("DB_USER", &res.DB.User),
		readEnvSecret("DB_PASS", &res.DB.Password),
	)
	var mailEnabled bool
	if err := readEnvBool("MAIL_ENABLED", &mailEnabled); err != nil {
		errs = append(errs, err)
	} else if mailEnabled {
		res.Mail = &MailConfig{}
		errs = append(errs,
			readEnvString("SMTP_SERVER", &res.Mail.Server),
			readEnvString("SMTP_CERT_HOSTNAME", &res.Mail.CertHostname),
			readEnvUint16("SMTP_PORT", &res.Mail.Port),
			readEnvSecret("SMTP_USER", &res.Mail.User),
			readEnvSecret("SMTP_PASS", &res.Mail.Password),
			readEnvString("MAIL_TO", &res.Mail.To),
			readEnvString("MAIL_FROM", &res.Mail.From),
			readEnvTemplate("MAIL_BODY_NEW_COMMENT", &res.Mail.NewCommentBodyTemplate),
		)
	}
	var rawCommentTagWhitelist []string
	if err := readEnvStringList("COMMENT_TAG_WHITELIST", &rawCommentTagWhitelist); err != nil {
		errs = append(errs, err)
	} else {
		res.CommentTagWhitelist = SetOf(slices.Values(rawCommentTagWhitelist))
	}
	var rawCommentAttributeWhitelist map[string][]string
	if err := readEnvJson("COMMENT_ATTRIBUTE_WHITELIST", &rawCommentAttributeWhitelist); err != nil {
		errs = append(errs, err)
	} else {
		res.CommentAttributeWhitelist = map[string]Set[string]{}
		for tag, attributes := range rawCommentAttributeWhitelist {
			res.CommentAttributeWhitelist[tag] = SetOf(slices.Values(attributes))
		}
	}

	if err := errors.Join(errs...); err != nil {
		return nil, err
	}
	return &res, nil
}

func readEnvString(key string, dest *string) error {
	var ok bool
	*dest, ok = os.LookupEnv(key)
	if !ok {
		return fmt.Errorf("%s not set", key)
	}
	return nil
}

func readEnvSecret(key string, dest *Secret) error {
	return readEnvString(key, (*string)(dest))
}

func readEnvUint16(key string, dest *uint16) error {
	var raw string
	if err := readEnvString(key, &raw); err != nil {
		return err
	}
	res, err := strconv.ParseUint(raw, 10, 16)
	if err != nil {
		return fmt.Errorf("parsing %s: %w", key, err)
	}
	*dest = uint16(res)
	return nil
}

func readEnvBool(key string, dest *bool) error {
	var raw string
	if err := readEnvString(key, &raw); err != nil {
		return err
	}
	res, err := strconv.ParseBool(raw)
	if err != nil {
		return err
	}
	*dest = res
	return nil
}

func readEnvStringList(key string, dest *[]string) error {
	var raw string
	if err := readEnvString(key, &raw); err != nil {
		return err
	}
	if raw == "" {
		*dest = nil
		return nil
	}
	*dest = strings.Split(raw, ",")
	return nil
}

func readEnvTemplate(key string, dest **template.Template) error {
	var raw string
	if err := readEnvString(key, &raw); err != nil {
		return err
	}
	res, err := template.New(key).Parse(raw)
	if err != nil {
		return fmt.Errorf("parsing %s: %w", key, err)
	}
	*dest = res
	return nil
}

func readEnvJson(key string, dest any) error {
	var raw string
	if err := readEnvString(key, &raw); err != nil {
		return err
	}
	if err := json.Unmarshal([]byte(raw), dest); err != nil {
		return fmt.Errorf("parsing %s JSON: %w", key, err)
	}
	return nil
}
