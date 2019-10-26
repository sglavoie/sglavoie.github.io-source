#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
import hashlib
import os

# Third-party imports
from pelican import __version__

# Absolute path to the directory where this file is being executed
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))


def get_cache_id(filename):
    md5 = hashlib.md5()

    with open(filename, "rb") as f:
        data = f.read()
        md5.update(data)

    return md5.hexdigest()


PELICAN_VERSION = __version__

ABOUT_VERSION = "0.9.0"  # major.minor.bug_fix
SITE_VERSION = "v0.20.0"  # major.minor.bug_fix
CURRENT_YEAR = datetime.today().year
DEFAULT_DATE_FORMAT = "%B %d, %Y"
LAST_UPDATE = datetime.now().strftime(DEFAULT_DATE_FORMAT)

AUTHOR = "Sébastien Lavoie"
SITENAME = "sglavoie.com"
SITEURL = "https://www.sglavoie.com"
SITESUBTITLE = f"The Learning Journey to the Summit of Commits | {AUTHOR}"
SITE_DESCRIPTION = """\
I document my journey as a learner in technology-related matters, \
explaining the challenges that I face while trying to become a better \
student. I teach the solutions that I find along the way so that it can \
benefit others too."""
DISQUS_SITENAME = "sglavoie"
TWITTER_USERNAME = "sgdlavoie"
THEME = "themes/SL"

PATH = "content"

TIMEZONE = "America/Mexico_City"

DEFAULT_LANG = "en"
LOCALE = "en_US.utf8"

MENUITEMS = [
    # path, id, icon
    ("/index.html", "home", '<i class="fas fa-home"></i>'),
    ("/tags.html", "tags", '<i class="fas fa-hashtag"></i>'),
    (
        "/learning-progress-2019.html",
        "learning",
        '<i class="fas fa-graduation-cap"></i>',
    ),
    ("/about.html", "about", '<i class="fas fa-info"></i>'),
]

PAGEITEMS = [
    (
        "/learning-progress-2019.html",
        "learning",
        '<i class="fas fa-graduation-cap"></i>',
    ),
    (
        "/learning-progress-2018-earlier.html",
        "learning",
        '<i class="fas fa-graduation-cap"></i>',
    ),
]

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]
TAG_CLOUD_STEPS = 5  # default 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_BADGE = True

# Default is 'random'.
# Other options are: alphabetically, alphabetically-rev, size, size-rev
TAG_CLOUD_SORTING = "size"


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

DIRECT_TEMPLATES = [
    "index",
    "categories",
    "authors",
    "archives",  # (default)
    # other HTML templates to render
    "tags",
    "about",
]

STATIC_PATHS = ["files", "images"]

DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = 5
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = "misc"
DISPLAY_CATEGORIES_ON_MENU = True
TYPOGRIFY = True
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Custom behavior below
BASE_CSS = get_cache_id(f"{THEME}/static/css/base.css")
PYGMENT_CSS = get_cache_id(f"{THEME}/static/css/pygment.css")
