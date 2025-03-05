package main

import (
	"context"
	"database/sql"
	"errors"
	"fmt"
	"time"

	"github.com/jackc/pgx/v5/pgconn"
	_ "github.com/jackc/pgx/v5/stdlib"
)

type database struct {
	db *sql.DB
}

func newDatabase(cfg *DBConfig) (*database, error) {
	dbURL := fmt.Sprintf("postgres://%s:%s@%s:%d/%s",
		cfg.User, cfg.Password, cfg.Host, cfg.Port, cfg.DB)
	db, err := sql.Open("pgx", dbURL)
	if err != nil {
		return nil, err
	}
	return &database{
		db: db,
	}, nil
}

type BlogComment struct {
	Time    time.Time `json:"time"`
	Author  string    `json:"author"`
	Content string    `json:"content"`
	URL     string    `json:"url"`
}

func (db *database) GetBlogComments(ctx context.Context, year int, articleSlug string) ([]BlogComment, error) {
	rows, err := db.db.QueryContext(ctx, "SELECT time, author, content, url FROM comments WHERE post = $1 AND approved = true ORDER BY time ASC", fmt.Sprintf("%d/%s", year, articleSlug))
	if err != nil {
		return nil, fmt.Errorf("query: %w", err)
	}
	var res []BlogComment
	for rows.Next() {
		var comment BlogComment
		if err := rows.Scan(&comment.Time, &comment.Author, &comment.Content, &comment.URL); err != nil {
			return nil, fmt.Errorf("scan %d: %w", len(res), err)
		}
		res = append(res, comment)
	}
	if err := rows.Err(); err != nil {
		return nil, fmt.Errorf("next: %w", err)
	}
	return res, nil
}

type dbComment struct {
	Author             string
	Email              string
	URL                sql.NullString
	UnsanitizedContent sql.NullString
	Content            string
	UserAgent          string
	Referrer           sql.NullString
	IP                 string
	Spam               bool
}

func (db *database) InsertBlogComment(ctx context.Context, year int, articleSlug string, c *dbComment) error {
	post := fmt.Sprintf("%d/%s", year, articleSlug)
	_, err := db.db.ExecContext(
		ctx,
		`INSERT INTO comments
		(post,  spam,  user_agent,   referrer,   author,   email,   url,  unsanitized_content,   content,   ip)
		VALUES
		(  $1,    $2,          $3,         $4,       $5,      $6,    $7,                   $8,        $9,  $10)`,
		post, c.Spam, c.UserAgent, c.Referrer, c.Author, c.Email, c.URL, c.UnsanitizedContent, c.Content, c.IP,
	)
	if err != nil {
		return fmt.Errorf("inserting into db: %w", err)
	}
	return nil
}

func (db *database) GetDownloadCount(ctx context.Context, path string) (int, error) {
	var res int
	if err := db.db.QueryRowContext(ctx, `SELECT downloads FROM downloads_v2 WHERE filepath = $1`, path).Scan(&res); err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			return 0, nil
		}
		return 0, err
	}
	return res, nil
}

func (db *database) IncrementDownloadCount(ctx context.Context, path string) error {
	_, err := db.db.ExecContext(ctx, `INSERT INTO downloads_v2 (filepath, downloads) VALUES ($1, 1)`, path)
	if err == nil {
		return nil
	}
	if pgErr := new(pgconn.PgError); errors.As(err, &pgErr) && pgErr.Code == "23505" {
		// unique violation -> already exists
		// since we never delete, this should not have any race conditions even without a transaction
		_, err = db.db.ExecContext(ctx, `UPDATE downloads_v2 SET downloads = downloads + 1 WHERE filepath = $1`, path)
		if err == nil {
			return nil
		}
		return fmt.Errorf("updating: %w", err)
	}
	return fmt.Errorf("inserting: %w", err)
	// TODO use upsert instead:
	// _, err := db.db.ExecContext(ctx, `INSERT INTO downloads_v2 (filepath, downloads) VALUES ($1, 1) ON CONFLICT (filepath) DO UPDATE SET downloads = downloads + 1`, path)
	// return err
}

type AdminBlogComment struct {
	BlogComment
	ID        int            `json:"id"`
	Post      string         `json:"post"`
	Spam      bool           `json:"spam"`
	UserAgent string         `json:"user_agent"`
	Referrer  sql.NullString `json:"referrer"`
	Email     string         `json:"email"`
	Approved  bool           `json:"approved"`
	IP        string         `json:"ip"`
}

func (db *database) GetUnapprovedComments(ctx context.Context) ([]AdminBlogComment, error) {
	rows, err := db.db.QueryContext(ctx, "SELECT time, author, content, url, id, post, spam, user_agent, referrer, email, approved, ip FROM comments WHERE approved = false ORDER BY time DESC")
	if err != nil {
		return nil, fmt.Errorf("query: %w", err)
	}
	var res []AdminBlogComment
	for rows.Next() {
		var comment AdminBlogComment
		if err := rows.Scan(&comment.Time, &comment.Author, &comment.Content, &comment.URL, &comment.ID, &comment.Post, &comment.Spam, &comment.UserAgent, &comment.Referrer, &comment.Email, &comment.Approved, &comment.IP); err != nil {
			return nil, fmt.Errorf("scan %d: %w", len(res), err)
		}
		res = append(res, comment)
	}
	if err := rows.Err(); err != nil {
		return nil, fmt.Errorf("next: %w", err)
	}
	return res, nil
}

func (db *database) ApproveComment(ctx context.Context, id int) (*dbComment, error) {
	var res dbComment
	err := db.db.QueryRowContext(ctx, `
		UPDATE comments
		SET approved = true
		WHERE id = $1
		RETURNING spam, author, email, url, unsanitized_content, content, user_agent, referrer, ip
		`, id).
		Scan(&res.Spam, &res.Author, &res.Email, &res.URL, &res.UnsanitizedContent, &res.Content, &res.UserAgent, &res.Referrer, &res.IP)
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			return nil, nil
		}
		return nil, fmt.Errorf("updating: %w", err)
	}
	return &res, nil
}

func (db *database) DeleteComment(ctx context.Context, id int) (*dbComment, error) {
	var res dbComment
	err := db.db.QueryRowContext(ctx, `
		DELETE FROM comments
		WHERE id = $1
		RETURNING spam, author, email, url, unsanitized_content, content, user_agent, referrer, ip
		`, id).
		Scan(&res.Spam, &res.Author, &res.Email, &res.URL, &res.UnsanitizedContent, &res.Content, &res.UserAgent, &res.Referrer, &res.IP)
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			return nil, nil
		}
		return nil, fmt.Errorf("deleting: %w", err)
	}
	return &res, nil
}
