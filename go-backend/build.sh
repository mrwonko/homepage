#!/usr/bin/env bash
set -eu
mkdir -p bin
go build -o bin/backend .
