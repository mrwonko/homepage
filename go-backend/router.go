package main

import (
	"context"
	"encoding/json"
	"errors"
	"log"
	"net/http"
	"strconv"
	"time"
)

const requestTimeout = 5 * time.Second

func newRouter(handlers *httpHandlers) http.Handler {
	const logUnhandledRequests = false
	mux := http.NewServeMux()
	mux.HandleFunc("OPTIONS /rest/blog/{year}/{article}/comments", handlers.blogComments)
	mux.HandleFunc("GET /rest/blog/{year}/{article}/comments", handlers.blogComments)
	mux.HandleFunc("POST /rest/blog/{year}/{article}/comments", handlers.blogComments)
	mux.HandleFunc("OPTIONS /rest/downloads/{path...}", handlers.downloadCount)
	mux.HandleFunc("GET /rest/downloads/{path...}", handlers.downloadCount)
	mux.HandleFunc("GET /internal/onDownload", unimplemented)
	mux.HandleFunc("GET /admin/rest/blog/comments/unapproved", unimplemented)
	mux.HandleFunc("POST /admin/rest/blog/comments/{id}", unimplemented)
	if logUnhandledRequests {
		mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
			log.Printf("fallthrough: %s %s", r.Method, r.URL.String())
			w.WriteHeader(http.StatusNotFound)
		})
	}
	return mux
}

type httpHandlers struct {
	db                   *database
	legacyDownloadCounts map[string]int
}

func (h *httpHandlers) blogComments(rw http.ResponseWriter, req *http.Request) {
	ctx, cancel := context.WithTimeout(req.Context(), requestTimeout)
	defer cancel()
	year, err := strconv.Atoi(req.PathValue("year"))
	if err != nil {
		rw.WriteHeader(http.StatusNotFound)
		return
	}
	articleSlug := req.PathValue("article")
	if articleSlug == "" {
		rw.WriteHeader(http.StatusNotFound)
	}
	switch req.Method {
	case http.MethodOptions:
		rw.Header().Add("Allow", "GET, POST, HEAD")
		rw.WriteHeader(http.StatusOK)
	case http.MethodGet, http.MethodHead:
		h.getBlogComments(ctx, rw, req, year, articleSlug)
	case http.MethodPost:
		// TODO
		rw.WriteHeader(http.StatusNotImplemented)
	default:
		rw.WriteHeader(http.StatusMethodNotAllowed)
	}
}

func (h *httpHandlers) getBlogComments(ctx context.Context, rw http.ResponseWriter, req *http.Request, year int, articleSlug string) {
	type BlogComments struct {
		Comments []BlogComment `json:"comments"`
	}
	comments, err := h.db.GetBlogComments(ctx, year, articleSlug)
	if err != nil {
		log.Printf("error getting blog comments for %d/%s: %s", year, articleSlug, err)
		rw.WriteHeader(http.StatusInternalServerError)
		return
	}
	res := BlogComments{
		Comments: comments,
	}
	rw.Header().Set("Content-Type", "application/json")
	if err := json.NewEncoder(rw).Encode(&res); err != nil && !errors.Is(err, req.Context().Err()) {
		log.Printf("error encoding blog comments: %s", err)
	}
}

func (h *httpHandlers) downloadCount(rw http.ResponseWriter, req *http.Request) {
	ctx, cancel := context.WithTimeout(req.Context(), requestTimeout)
	defer cancel()
	path := req.PathValue("path")
	if path == "" {
		rw.WriteHeader(http.StatusNotFound)
	}
	switch req.Method {
	case http.MethodOptions:
		rw.Header().Add("Allow", "GET, HEAD")
		rw.WriteHeader(http.StatusOK)
	case http.MethodGet, http.MethodHead:
		dbCount, err := h.db.GetDownloadCount(ctx, path)
		if err != nil {
			log.Printf("error getting download count for %q: %s", path, err)
			rw.WriteHeader(http.StatusInternalServerError)
			return
		}
		res := struct {
			Downloads int `json:"downloads"`
		}{
			Downloads: dbCount + h.legacyDownloadCounts[path],
		}
		rw.Header().Set("Content-Type", "application/json")
		if err := json.NewEncoder(rw).Encode(&res); err != nil && !errors.Is(err, req.Context().Err()) {
			log.Printf("error encoding blog comments: %s", err)
		}
	default:
		rw.WriteHeader(http.StatusMethodNotAllowed)
	}
}

func unimplemented(rw http.ResponseWriter, req *http.Request) {
	log.Printf("unimplemented: %s %s", req.Method, req.URL)
	rw.WriteHeader(http.StatusNotImplemented)
}
