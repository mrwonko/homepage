package main

import (
	"log"
	"net/http"
	"strconv"
)

func newRouter(handlers *httpHandlers) http.Handler {
	const logUnhandledRequests = false
	mux := http.NewServeMux()
	mux.HandleFunc("OPTIONS /rest/blog/{year}/{article}/comments", handlers.blogComments)
	mux.HandleFunc("GET /rest/blog/{year}/{article}/comments", handlers.blogComments)
	mux.HandleFunc("POST /rest/blog/{year}/{article}/comments", handlers.blogComments)
	if logUnhandledRequests {
		mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
			log.Printf("fallthrough: %s %s", r.Method, r.URL.String())
			w.WriteHeader(http.StatusNotFound)
		})
	}
	return mux
}

type httpHandlers struct {
	db *database
}

func (h *httpHandlers) blogComments(rw http.ResponseWriter, req *http.Request) {
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
		// TODO
		rw.WriteHeader(http.StatusNotImplemented)
		_ = year
	case http.MethodPost:
		// TODO
		rw.WriteHeader(http.StatusNotImplemented)
	default:
		rw.WriteHeader(http.StatusMethodNotAllowed)
	}
}
