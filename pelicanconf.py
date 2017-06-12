#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ben Hoff'
SITENAME = "Ben's Blog"
SITEURL = 'http://benhoff.net'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = 'themes/base_theme'

LINKS = (('Github', 'https://github.com/benhoff'),
         ('Community', 'https://community.benhoff.net'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = [('Archives', '%s/archives.html' % SITEURL)]
