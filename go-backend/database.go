package main

import (
	"database/sql"
	"fmt"

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

// TODO: use the new unsanitized_content column to store the original comment,
// for better spam detection and so I can fix sanitization errors manually, if need be.
