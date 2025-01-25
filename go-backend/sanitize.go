package main

import "strings"

var sanitizeReplacer = strings.NewReplacer("<", "&lt;", ">", "&gt;")

func sanitizeHTML(unsanitizedHTML string, tagWhitelist Set[string], attributeWhitelist map[string]Set[string]) string {
	// TODO implement whitelist
	_, _, _ = unsanitizedHTML, tagWhitelist, attributeWhitelist
	return sanitizeReplacer.Replace(unsanitizedHTML)
}
