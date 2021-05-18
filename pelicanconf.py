"""Pelican's main configuration file"""
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from pelican import __version__

from datetime import datetime

PELICAN_VERSION = __version__

# Pelican-specific settings
PATH = "content"

STATIC_PATHS = ["files", "images"]

DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = 5

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = "misc"
DISPLAY_CATEGORIES_ON_MENU = True

# Allows to automatically update to today's date for a page that does not
# specify a date
t = datetime.today()
DEFAULT_DATE = (t.year, t.month, t.day, t.hour, t.minute, t.second)

TYPOGRIFY = True

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Site-specific
AUTHOR = "Sébastien Lavoie"
DEFAULT_LANG = "en"
DISQUS_SITENAME = "sglavoie"
LOCALE = "en_US.utf8"
SITENAME = "sglavoie.com"
SITEURL = "https://www.sglavoie.com"
TIMEZONE = "America/Mexico_City"

# Theme-specific
THEME = "themes/svbhack"
USER_LOGO_URL = SITEURL + "/theme/images/logo.png"

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["readtime", "extract_toc"]

# `fenced_code` enables the following syntax for code blocks and make it
# possible to use special symbols, among other things:
# ~~~~{.language_name_here}
# code goes here
# ~~~~
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

# Feed generation is usually not desired when developing
# FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ATOM = None
FEED_ATOM_URL = None
FEED_RSS = None
FEED_ALL_RSS = "feeds/sglavoie.rss.xml"
CATEGORY_FEED_RSS = None
