#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Willi Schinmeyer"
SITENAME = "mrwonko's blog"
# hack for this to work both locally and deployed
SITEURL = "http://mrwonko.de"

#   Plugins

PLUGIN_PATHS = [ "plugins" ]
PLUGINS = [ "metadata_links", "article_types" ]
LINK_METADATA = [ 'link', 'thumbnail' ]

#   Input Paths

PATH = "content"
# path to files that are not to be processed, just copied verbatim (automatically excludes articles)
ARTICLE_PATHS = [ "blog", "tutorials", "downloads" ]
PAGE_PATHS = [ "pages" ]
STATIC_PATHS = ARTICLE_PATHS + [ "static" ]

#   Templates to generate besides articles/pages/static

DIRECT_TEMPLATES = [
    "index",
    "authors"
]
PAGINATED_DIRECT_TEMPLATES = [
]

#   Output Filenames

# where to put generated articles; using the new "type" makes that metadata mandatory.
ARTICLE_SAVE_AS = "{type}/{date:%Y}/{slug}.html"
# how to link to them (useful e.g. for omitting /index.html)
ARTICLE_URL = ARTICLE_SAVE_AS

DRAFT_SAVE_AS = "{type}/drafts/{slug}.html"

CATEGORY_SAVE_AS = "{type}/category/{slug}.html"
CATEGORY_URL = "{type}/category/{slug}.html"

TAG_SAVE_AS = "{type}/tag/{slug}.html"
TAG_URL = "{type}/tag/{slug}.html"

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
        'index_title': "mrwonko's blog",
        'index_save_as': "blog/index.html",
        'index_template': "index",#"blog_index",
        'index_paginate': True,
        
        'tags_title': "mrwonko's blog - tags",
        'tags_save_as': "blog/tags.html",
        'tags_template': "tags",
        'tags_paginate': True,
        
        'categories_title': "mrwonko's blog - categories",
        'categories_save_as': "blog/categories.html",
        'categories_template': "categories",
        'categories_paginate': True,
        
        'article_template': "article",
        
        'feed_atom': "feeds/blog.atom",
        'feed_rss': "feeds/blog.rss"
    },
    "tutorials": {
        'index_title': "mrwonko's tutorials",
        'index_save_as': "tutorials/index.html",
        'index_template': "index",#"tutorial_index",
        'index_paginate': False,
        
        'tags_title': "mrwonko's tutorials - tags",
        'tags_save_as': "tutorials/tags.html",
        'tags_template': "tags",
        'tags_paginate': False,
        
        'categories_save_as': None,
        
        'article_template': "article",#"tutorial",
        
        'feed_atom': None,
        'feed_rss': None
    },
    "downloads": {
        'index_title': "mrwonko's downloads",
        'index_save_as': "downloads/index.html",
        'index_template': "index",#"download_index",
        'index_paginate': False,
        
        'tags_title': "mrwonko's downloads - tags",
        'tags_save_as': "downloads/tags.html",
        'tags_template': "tags",
        'tags_paginate': False,
        
        'categories_title': "mrwonko's downloads - categories",
        'categories_save_as': "downloads/categories.html",
        'categories_template': "categories",
        'categories_paginate': False,
        
        'article_template': "download",
        
        'feed_atom': "feeds/downloads.atom",
        'feed_rss': "feeds/downloads.rss"
    }
}

PAGINATE_AUTHOR_PAGES = False

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
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
