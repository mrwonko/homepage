#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Willi Schinmeyer"
SITENAME = "mrwonko.de"
# hack for this to work both locally and deployed
SITEURL = "http://mrwonko.de"

#   Plugins

PLUGIN_PATHS = [ "plugins" ]
PLUGINS = [ "metadata_links", "article_types" ]
LINK_METADATA = [ 'thumbnail' ]

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
    ("downloads", "downloads/index.html")
]
DISPLAY_CATEGORIES_ON_MENU = False
PAGE_ORDER_BY = 'page-order'

# Credits
LINKS = [
    ( "Pelican", "http://getpelican.com" ),
    ( "Bootstrap", "http://getbootstrap.com" ),
    ( "Font Awesome", "http://fontawesome.io" ),
    ( "Git", "http://git-scm.com" ),
    ( "nginx", "http://nginx.org" )
]

# Social widget
SOCIAL = [
    ( "Twitter", "mrw-fa-twitter", "@mrwonko", "https://twitter.com/mrwonko" ),
    ( "Github", "mrw-fa-github", "mrwonko", "http://github.com/mrwonko/" ),
    ( "Youtube", "mrw-fa-youtube", "mrwonko", "https://www.youtube.com/user/mrwonko/" ),
    ( "Steam", "mrw-fa-steam", "mrwonko", "http://steamcommunity.com/id/mrwonko/" ),
    ( "LinkedIn", "mrw-fa-linkedin", "Willi Schinmeyer", "https://www.linkedin.com/profile/view?id=67044848" ),
]

#   Article Types

TYPE_SETTINGS = {
    "blog": {
        'title': "blog",
        'tab': "blog",
        'parent_breadcrumbs': [],
        'comments': True,
        
        'index_save_as': "blog/index.html",
        'index_template': "blog_index",
        'index_paginate': True,
        
        'tags_save_as': "blog/tags.html",
        'tags_template': "tags",
        'tags_paginate': True,
        
        'categories_save_as': "blog/categories.html",
        'categories_template': "categories",
        'categories_paginate': True,
        
        'article_template': "article",
        
        'feed_atom': "feeds/blog.atom",
        'feed_rss': "feeds/blog.rss"
    },
    "tutorials/darth-arth": {
        'title': "Darth-Arth.de Archiv",
        'tab': "tutorials",
        'parent_breadcrumbs': [ ( "tutorials", "tutorials/index.html" ) ],
        'hide_date': True,
        
        'index_save_as': "tutorials/darth-arth/index.html",
        'index_template': "tutorial_index",
        'index_paginate': False,
        
        'tags_save_as': "tutorials/darth-arth/tags.html",
        'tags_template': "tags",
        'tags_paginate': False,
        
        'categories_save_as': None,
        
        'article_template': "article",
        'article_footer': u'Alle Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: © 2000 - 2003 (Artur L.) Nur zur privaten Nutzung. Kopieren nicht gestattet. Hier gespiegelt mit freundlicher Erlaubnis von Darth-Arth a.k.a. MetalBeast (<a href="http://www.3d-get.de/metalbeast">Website</a>).',
        
        'feed_atom': None,
        'feed_rss': None
    },
    "downloads": {
        'title': "downloads",
        'tab': "downloads",
        'parent_breadcrumbs': [],
        
        'index_save_as': "downloads/index.html",
        'index_template': "download_index",
        'index_paginate': False,
        
        'tags_save_as': "downloads/tags.html",
        'tags_template': "tags",
        'tags_paginate': False,
        
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
