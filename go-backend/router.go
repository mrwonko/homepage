package main

import (
	"context"
	"database/sql"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
	"strconv"
	"strings"
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
	mux.HandleFunc("GET /internal/onDownload", handlers.onDownload)
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
	db                        *database
	legacyDownloadCounts      map[string]int
	akismet                   *Akismet
	mailer                    *Mailer
	commentTagWhitelist       Set[string]
	commentAttributeWhitelist map[string]Set[string]
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
		h.postBlogComment(ctx, rw, req, year, articleSlug)
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

func (h *httpHandlers) postBlogComment(ctx context.Context, rw http.ResponseWriter, req *http.Request, year int, articleSlug string) {
	type Comment struct {
		Author  string `json:"author"`
		Content string `json:"content"`
		Email   string `json:"email"`
		URL     string `json:"url"` // optional
	}
	var reqComment Comment
	if err := json.NewDecoder(req.Body).Decode(&reqComment); err != nil {
		rw.WriteHeader(http.StatusBadRequest)
		fmt.Fprintf(rw, "error decoding request body json: %s", err)
		return
	}
	var missing []string
	for _, mandatoryField := range []struct {
		field string
		value string
	}{
		{field: "author", value: reqComment.Author},
		{field: "content", value: reqComment.Content},
		{field: "email", value: reqComment.Email},
		// URL is optional
	} {
		if mandatoryField.value == "" {
			missing = append(missing, mandatoryField.field)
		}
	}
	if len(missing) > 0 {
		rw.WriteHeader(http.StatusBadRequest)
		fmt.Fprintf(rw, "%s must not be empty", strings.Join(missing, ", "))
		return
	}
	spammy, err := h.akismet.Check(ctx)
	if err != nil {
		log.Printf("error performing akismet spam check: %s", err)
		// this is non-fatal
		spammy = false
	}
	content := sanitizeHTML(reqComment.Content, h.commentTagWhitelist, h.commentAttributeWhitelist)
	content = strings.ReplaceAll(content, "\n", "<br/>\n")
	comment := &dbComment{
		Author:             reqComment.Author,
		Email:              reqComment.Email,
		URL:                sql.NullString{String: reqComment.URL, Valid: reqComment.URL != ""},
		UnsanitizedContent: reqComment.Content,
		Content:            content,
		UserAgent:          req.UserAgent(),
		Referrer:           req.Referer(),
		IP:                 req.RemoteAddr,
		Spam:               spammy,
	}
	err = h.db.InsertBlogComment(ctx, year, articleSlug, comment)
	if err != nil {
		log.Printf("error inserting comment %d/%s %v: %s", year, articleSlug, comment, err)
		return
	}
	err = h.mailer.SendCommentNotification(ctx, year, articleSlug, comment)
	if err != nil {
		log.Printf("error sending comment notificaton email: %s", err)
		return
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

func (h *httpHandlers) onDownload(rw http.ResponseWriter, req *http.Request) {
	ctx, cancel := context.WithTimeout(req.Context(), requestTimeout)
	defer cancel()
	args := req.URL.Query()
	file := strings.TrimPrefix(args.Get("file"), "/")
	if file == "" {
		log.Printf("error: onDownload called without file")
		return
	}
	method := args.Get("method")
	if method != "GET" {
		log.Printf("error: onDownload %q called with unexpected method %s", file, method)
	}
	completion := args.Get("completion")
	if completion != "OK" {
		// no need to report incomplete downloads, probably
		return
	}
	status := args.Get("status")
	if status == "" || status[0] != '2' {
		// this probably means someone got a file not found, which might be their error
		log.Printf("onDownload %q got status %s", file, status)
		return
	}
	if err := h.db.IncrementDownloadCount(ctx, file); err != nil {
		log.Printf("error incrementing download count for %q: %s", file, err)
	}
}

func unimplemented(rw http.ResponseWriter, req *http.Request) {
	log.Printf("unimplemented: %s %s", req.Method, req.URL)
	rw.WriteHeader(http.StatusNotImplemented)
}
