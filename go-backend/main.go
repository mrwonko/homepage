package main

import (
	"log"
	"os"
)

func main() {
	os.Exit(mainWithExitCode())
}

func mainWithExitCode() int {
	cfg, err := configFromEnv()
	if err != nil {
		log.Printf("invalid config: %s", err)
		return 1
	}
	_ = cfg
	// TODO start server
	return 0
}
