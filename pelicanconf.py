#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Willi Schinmeyer'
SITENAME = u"mrwonko's blog"
SITEURL = 'http://mrwonko.de'

#   Plugins

PLUGIN_PATHS = [ "plugins" ]
PLUGINS = [ "article_types" ]

#   Input Paths

PATH = 'content'
# path to files that are not to be processed, just copied verbatim (automatically excludes articles)
ARTICLE_PATHS = [ 'blog', 'tutorials' ]
PAGE_PATHS = [ 'pages' ]
STATIC_PATHS = ARTICLE_PATHS + [ 'static' ]

#   Templates to generate besides articles/pages/static

DIRECT_TEMPLATES = [
    "index",
    "authors"
]
PAGINATED_DIRECT_TEMPLATES = [
]

#   Output Filenames

# where to put generated articles; using the new "type" makes that metadata mandatory.
ARTICLE_SAVE_AS = '{type}/{date:%Y}/{slug}.html'
# how to link to them (useful e.g. for omitting /index.html)
ARTICLE_URL = ARTICLE_SAVE_AS

DRAFT_SAVE_AS = '{type}/drafts/{slug}.html'

#   Theme

# THEME = "notmyidea"
# THEME = "simple"
THEME = "themes/wonky2015"

#   Menu

MENUITEMS = [
    ("home", "index.html"),
    ("blog", "blog/index.html"),
    ("downloads", "downloads/index.html"),
    ("tutorials", "tutorials/index.html")
]
DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/')
    ,('Python.org', 'http://python.org/')
    ,('Jinja2', 'http://jinja.pocoo.org/')
    #,('You can modify those links in your config file', '#')
    )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

#   Article Types

TYPE_SETTINGS = {
    "blog": {
        "index_save_as": "blog/index.html",
        "index_template": "index",#"blog_index",
        
        "tags_save_as": "blog/tags.html",
        "tags_template": "tags",
        
        "categories_save_as": "blog/categories.html",
        "categories_template": "categories",
        
        "article_template": "article",
        
        "feed_atom": "feeds/blog.atom",
        "feed_rss": "feeds/blog.rss"
    },
    "tutorial": {
        "index_save_as": "tutorials/index.html",
        "index_template": "index",#"tutorial_index",
        
        "tags_save_as": "tutorials/tags.html",
        "tags_template": "tags",
        
        "categories_save_as": None,
        
        "article_template": "article",#"tutorial",
        
        "feed_atom": None,
        "feed_rss": None
    },
    "download": {
        "index_save_as": "downloads/index.html",
        "index_template": "index",#"download_index",
        
        "tags_save_as": "tutorials/tags.html",
        "tags_template": "tags",
        
        "categories_save_as": "tutorials/categories.html",
        "categories_template": "categories",
        
        "article_template": "article",#"download",
        
        "feed_atom": "feeds/downloads.atom",
        "feed_rss": "feeds/downloads.rss"
    }
}

#   Feeds

# feeds handled per-type, so no global ones
FEED_RSS = None
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#   Misc

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
