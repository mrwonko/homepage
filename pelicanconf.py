#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Willi Schinmeyer'
SITENAME = u"mrwonko's blog"
SITEURL = 'http://mrwonko.de'

PATH = 'content'
# path to files that are not to be processed, just copied verbatim (automatically excludes articles)
STATIC_PATHS = [ 'blog' ]
ARTICLE_PATHS = [ 'blog' ]
PAGE_PATHS = [ 'pages' ]
# where to put generated blog entries
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m-%d}-{slug}.html'
# how to link to them (useful e.g. for omitting /index.html)
ARTICLE_URL = 'blog/{date:%Y}/{date:%m-%d}-{slug}.html'

# THEME = "notmyidea"
# THEME = "simple"
THEME = "themes/wonky2015"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/')
    ,('Python.org', 'http://python.org/')
    ,('Jinja2', 'http://jinja.pocoo.org/')
    #,('You can modify those links in your config file', '#')
    )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
