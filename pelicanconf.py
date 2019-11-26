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
DISPLAY_FOOTER = False
THEME = 'themes/pelican-blue'

LINKS = (('Community', 'https://community.benhoff.net'),
         ('Github', 'https://github.com/benhoff'),
         ('Youtube', 'https://www.youtube.com/channel/UChWbNrHQHvKK6paclLp7WYw'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = [('Archives', '%s/archives.html' % SITEURL),
             ('Community', 'https://community.benhoff.net')]

TYPOGRIFY = True
STATIC_PATHS = ['extra/CNAME', 'images', 'extra/favicon.ico', 'extra/ads.txt']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/ads.txt': {'path': 'ads.txt'},}


# pelican-ipynb settings
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS=['plugins',]
PLUGINS = ['ipynb.markup', 'sitemap']
IGNORE_FILES = ['.ipynb_checkpoints']

SITEMAP = {'exclude': ['tag/',],
           'format': 'xml'}
