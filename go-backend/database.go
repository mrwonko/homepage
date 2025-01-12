package main

import (
	"context"
	"database/sql"
	"fmt"
	"time"

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

// TODO: use the new unsanitized_content column to store the original comment,
// for better spam detection and so I can fix sanitization errors manually, if need be.

func (db *database) GetDownloadCount(ctx context.Context, path string) (int, error) {
	// FIXME this is mad, just keep a counter, don't have one row per download
	var res int
	if err := db.db.QueryRowContext(ctx, `SELECT COUNT(*) FROM downloads JOIN download_names ON downloads.download = download_names.id WHERE download_names.name = $1`, path).Scan(&res); err != nil {
		return 0, err
	}
	return res, nil
}
