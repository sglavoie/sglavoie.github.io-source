#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from pelican import __version__

PELICAN_VERSION = __version__

SITE_VERSION = 'v0.3.4'
CURRENT_YEAR = datetime.today().year

AUTHOR = 'Sébastien Lavoie'
SITENAME = 'sglavoie.com'
SITEURL = ''
SITESUBTITLE = ''
DISQUS_SITENAME = 'sglavoie'
TWITTER_USERNAME = 'sgdlavoie'
THEME = 'themes/SL'
ABOUT_VERSION = '0.1.0'

PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# STATIC_PATHS = [
    # 'pictures',
    # 'extra/robots.txt',
    # ]


DIRECT_TEMPLATES = [
    'index', 'categories', 'authors', 'archives',  # (default)
    'tags', 'about',  # other HTML templates to render
]

DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = 5
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DISPLAY_CATEGORIES_ON_MENU = True
TYPOGRIFY = False
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
