package main

import "testing"

func Test_sanitizeHTML(t *testing.T) {
	tests := []struct {
		name               string
		input              string
		tagWhitelist       Set[string]
		attributeWhitelist map[string]Set[string]
		want               string
	}{
		{
			name:  "empty whitelist",
			input: "<i>illegal</i> <b>instructions</b>",
			want:  "&lt;i&gt;illegal&lt;/i&gt; &lt;b&gt;instructions&lt;/b&gt;",
		},
		// TODO tests for non-empty whitelist, once implemented
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := sanitizeHTML(tt.input, tt.tagWhitelist, tt.attributeWhitelist)
			if got != tt.want {
				t.Errorf("got %q, want %q", got, tt.want)
			}
		})
	}
}
