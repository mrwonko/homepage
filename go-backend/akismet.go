package main

import (
	"context"
	"time"
)

type Akismet struct {
	APIKey Secret
}

func (a *Akismet) Check(ctx context.Context) (spammy bool, err error) {
	const akismetTimeout = 5 * time.Second
	ctx, cancel := context.WithTimeout(ctx, akismetTimeout)
	defer cancel()
	// TODO
	return false, nil
}
