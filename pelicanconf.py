#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os.path as op


AUTHOR = u'Faisal Khan'
SITENAME = u"Faisal's Notes"
TAGLINE = "Data | Code | Visualization"
SITEURL = 'http://faisalnotes.com'
PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


THEME = 'themes/pure-tech'

STATIC_PATHS = [
	'images',
	'extra/CNAME'
]

EXTRA_PATH_METADATA = {
    'images/favicon.png': {'path': 'favicon.png'},
    'extra/CNAME' : {'path': 'CNAME'}
}

DATE_FORMATS = {
    'en': '%Y-%m-%d',
}

SITESUBTITLES = ('Faisal\'s Notes', '')

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
PLUGIN_PATHS = ['pelican-plugins', 'plugins']

DIRECT_TEMPLATES = ('index', 'archives')
ARCHIVES_SAVE_AS = 'archives/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
