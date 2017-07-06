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

LINKS = (('Community', 'https://community.benhoff.net'),
         ('Github', 'https://github.com/benhoff'),
         ('Youtube', 'https://www.youtube.com/channel/UChWbNrHQHvKK6paclLp7WYw'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = [('Archives', '%s/archives.html' % SITEURL),
             ('Community', 'https:community.benhoff.net')]

TYPOGRIFY = True
STATIC_PATHS = ['extra/CNAME', 'images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'}}


# pelican-ipynb settings
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS=['plugins',]
PLUGINS = ['ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']
