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
	mux.HandleFunc("GET /admin/rest/blog/comments/unapproved", handlers.adminUnapprovedComments)
	mux.HandleFunc("POST /admin/rest/blog/comments/{id}", handlers.adminModerateComment)
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
	content := sanitizeHTML(reqComment.Content, h.commentTagWhitelist, h.commentAttributeWhitelist)
	content = strings.ReplaceAll(content, "\n", "<br/>\n")
	comment := &dbComment{
		Author:             reqComment.Author,
		Email:              reqComment.Email,
		URL:                sql.NullString{String: reqComment.URL, Valid: reqComment.URL != ""},
		UnsanitizedContent: sql.NullString{String: reqComment.Content, Valid: true},
		Content:            content,
		UserAgent:          req.UserAgent(),
		Referrer:           sql.NullString{String: req.Referer(), Valid: req.Referer() != ""},
		IP:                 req.RemoteAddr,
	}
	spammy, err := h.akismet.Check(ctx, comment)
	if err != nil {
		log.Printf("error performing akismet spam check: %s", err)
		// this is non-fatal
		spammy = Ham
	}
	comment.Spam = spammy == Spam
	if spammy == Discard {
		// definite spam doesn't even reach the DB
		log.Printf("discarding spam: %#v", comment)
		return
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
			Downloads: dbCount,
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

func (h *httpHandlers) adminUnapprovedComments(rw http.ResponseWriter, req *http.Request) {
	// auth is handled by the reverse proxy, so we assume proper authentication here
	ctx, cancel := context.WithTimeout(req.Context(), requestTimeout)
	defer cancel()
	switch req.Method {
	case http.MethodOptions:
		rw.Header().Add("Allow", "GET, HEAD")
		rw.WriteHeader(http.StatusOK)
	case http.MethodGet, http.MethodHead:
		comments, err := h.db.GetUnapprovedComments(ctx)
		if err != nil {
			log.Printf("error getting unapproved comments: %s", err)
			rw.WriteHeader(http.StatusInternalServerError)
			return
		}
		res := struct {
			Comments []AdminBlogComment `json:"comments"`
		}{
			Comments: comments,
		}
		rw.Header().Set("Content-Type", "application/json")
		if err := json.NewEncoder(rw).Encode(&res); err != nil && !errors.Is(err, req.Context().Err()) {
			log.Printf("error encoding blog comments: %s", err)
		}
	default:
		rw.WriteHeader(http.StatusMethodNotAllowed)
	}
}

func (h *httpHandlers) adminModerateComment(rw http.ResponseWriter, req *http.Request) {
	// auth is handled by the reverse proxy, so we assume proper authentication here
	ctx, cancel := context.WithTimeout(req.Context(), requestTimeout)
	defer cancel()
	id, err := strconv.Atoi(req.PathValue("id"))
	if err != nil {
		rw.WriteHeader(http.StatusNotFound)
		return
	}
	type RespBody map[string]any
	respond := func(body RespBody) {
		rw.Header().Set("Content-Type", "application/json")
		if err := json.NewEncoder(rw).Encode(&body); err != nil && !errors.Is(err, req.Context().Err()) {
			log.Printf("error encoding response: %s", err)
		}
	}
	switch req.Method {
	case http.MethodOptions:
		rw.Header().Add("Allow", "POST")
		rw.WriteHeader(http.StatusOK)
	case http.MethodPost:
		type ReqBody struct {
			Action string `json:"action"`
		}
		var reqBody ReqBody
		if err := json.NewDecoder(req.Body).Decode(&reqBody); err != nil {
			rw.WriteHeader(http.StatusBadRequest)
			fmt.Fprintf(rw, "error decoding request body json: %s", err)
			return
		}
		switch reqBody.Action {
		case "delete":
			comment, err := h.db.DeleteComment(ctx, id)
			if err != nil {
				log.Printf("error deleting comment %d: %s", id, err)
				respond(RespBody{"success": false, "error": err.Error()})
				return
			}
			resp := RespBody{"success": comment != nil}
			if comment == nil {
				resp["error"] = "not found"
			}
			respond(resp)
			return
		case "approve":
			comment, err := h.db.ApproveComment(ctx, id)
			if err != nil {
				log.Printf("error approving comment %d: %s", id, err)
				rw.WriteHeader(http.StatusInternalServerError)
				return
			}
			if comment == nil {
				respond(RespBody{
					"success": false,
					"error":   "not found",
				})
				return
			}
			if comment.Spam {
				// report false positive to akismet
				err := h.akismet.SubmitHam(ctx, comment)
				if err != nil {
					log.Printf("error reporting false positive to akismet: %s", err)
				}
			}
			respond(RespBody{"success": true})
			return
		case "spam":
			comment, err := h.db.DeleteComment(ctx, id)
			if err != nil {
				log.Printf("error deleting spam comment %d: %s", id, err)
				respond(RespBody{"success": false, "error": err.Error()})
				return
			}
			if comment == nil {
				respond(RespBody{"success": false, "error": "not found"})
				return
			}
			if !comment.Spam {
				// report false negative to akismet
				err = h.akismet.SubmitSpam(ctx, comment)
				if err != nil {
					log.Printf("error reporting false negative to akismet: %s", err)
				}
			}
			respond(RespBody{"success": true})
			return
		}
	default:
		rw.WriteHeader(http.StatusMethodNotAllowed)
	}
}
