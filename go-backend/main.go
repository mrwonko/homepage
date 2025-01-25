package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"
	"os/signal"
	"time"
)

func main() {
	ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt)
	exitCode := mainWithExitCode(ctx)
	cancel()
	os.Exit(exitCode)
}

func mainWithExitCode(ctx context.Context) int {
	cfg, err := configFromEnv()
	if err != nil {
		log.Printf("invalid config: %s", err)
		return 1
	}

	db, err := newDatabase(&cfg.DB)
	if err != nil {
		log.Printf("connecting to DB: %s", err)
		return 2
	}

	akismet := &Akismet{
		APIKey: cfg.AkismetKey,
	}
	mailer := &Mailer{
		config: cfg.Mail,
	}

	// setup http server
	handlers := &httpHandlers{
		db:                        db,
		akismet:                   akismet,
		mailer:                    mailer,
		commentTagWhitelist:       cfg.CommentTagWhitelist,
		commentAttributeWhitelist: cfg.CommentAttributeWhitelist,
	}
	router := newRouter(handlers)
	srv := &http.Server{
		Addr:                         fmt.Sprintf("%s:%d", cfg.ListenHost, cfg.ListenPort),
		Handler:                      router,
		DisableGeneralOptionsHandler: true,
	}

	// start http server
	ctx, initiateShutdown := context.WithCancel(ctx)
	log.Printf("launching HTTP server")
	go func() {
		defer initiateShutdown() // end main on server error
		err := srv.ListenAndServe()
		log.Printf("http.Server.ListenAndServe: %v", err)
	}()

	// wait for shutdown request
	<-ctx.Done()
	gracefulShutdownCtx, terminateGracefulShutdown := context.WithTimeout(context.WithoutCancel(ctx), 5*time.Second)
	err = srv.Shutdown(gracefulShutdownCtx)
	terminateGracefulShutdown()
	log.Printf("http.Server.Shutdown: %v", err)
	return 0
}
