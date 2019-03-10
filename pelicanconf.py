#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from pelican import __version__
import glob
import os
import subprocess

# TODO: Until I figure out how to create a plugin, functions appear here
def current_path():
    '''Return a string containing the absolute path to the directory
    where this file is being executed.'''
    return os.path.dirname(os.path.realpath(__file__))

def num_articles():
    '''Return the number of articles that match the following regex as
    an integer.'''
    return len(glob.glob('./content/**/[0-9][0-9][0-9][0-9]*.md'))


def read_tree():
    '''Execute `tree` command to output HTML with colors. Filter out the
    noise and keep the essential part as a template to be included in
    `tree.html`.'''
    subprocess.run(f'tree -C -H . ./output/ > ./tree.txt', shell=True)
    body = False
    extracted_tree = []
    with open('tree.txt') as f:
        for line in f:
            if not body:
                if '<body>' in line:
                    body = True
            else:
                if '</body>' in line:
                    break
                extracted_tree.append(line)
    with open('./themes/SL/templates/tree_content.html', 'w') as f:
        for line in extracted_tree:
            f.write(line)


def daily_stats():
    '''Execute `Gitstats` once a day based on the date found in
    `stats_counter.txt`. Very simple with a caveat: it won't check if
    there are new commits on the same day if stats have already been
    generated on that day.'''
    today = datetime.today().strftime('%Y%m%d')
    with open('stats_counter.txt') as f:
        content = f.readline().strip()
    if content != today:
        current_loc = current_path()
        cmd = ["gitstats", "-c", "project_name='sglavoie.com'",
               f"{current_loc}", f"{current_loc}/output/stats/"]
        subprocess.run(cmd)
        with open('stats_counter.txt', 'w') as f:
            f.write(today)


daily_stats()
read_tree()

NUM_ARTICLES = num_articles()

PELICAN_VERSION = __version__

ABOUT_VERSION = '0.3.0'
SITE_VERSION = 'v0.11.0'
CURRENT_YEAR = datetime.today().year
DEFAULT_DATE_FORMAT = '%B %d, %Y @ %H:%M CST'
LAST_UPDATE = datetime.now().strftime(DEFAULT_DATE_FORMAT)

AUTHOR = 'Sébastien Lavoie'
SITENAME = 'sglavoie.com'
SITEURL = 'https://www.sglavoie.com'
SITESUBTITLE = f'The Learning Journey to the Summit of Commits | {AUTHOR}'
SITE_DESCRIPTION = (
        'Provide useful information while documenting my journey as'
        ' a learner in technology-related matters. Tech journal with'
        ' the specific goal of explaining the challenges that I will'
        ' inevitably face while trying to become a better student and most'
        ' importantly, it will be a reference to the solutions that I'
        ' found along the way so that it can benefit others too.')
DISQUS_SITENAME = 'sglavoie'
TWITTER_USERNAME = 'sgdlavoie'
THEME = 'themes/SL'

PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'en'
LOCALE = 'en_US'

MENUITEMS = [
    # path, id, icon
    ('/index.html', 'home', '<i class="fas fa-home"></i>'),
    ('/tags.html', 'tags', '<i class="fas fa-hashtag"></i>'),
    ('/learning-progress.html', 'learning',
     '<i class="fas fa-graduation-cap"></i>'),
    ('/about.html', 'about', '<i class="fas fa-info"></i>')
]

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]
TAG_CLOUD_STEPS = 5  # default 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_BADGE = True

# Default is 'random'.
# Other options are: alphabetically, alphabetically-rev, size, size-rev
TAG_CLOUD_SORTING = 'size'


# `fenced_code` enables the following syntax for code blocks and make it
# possible to use special symbols, among other things:
# ~~~~{.language_name_here}
# code goes here
# ~~~~
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
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
FEED_ALL_RSS = 'feeds/sglavoie.rss.xml'
CATEGORY_FEED_RSS = None

DIRECT_TEMPLATES = [
    'index', 'categories', 'authors', 'archives',  # (default)
    'tags', 'about', 'tree'  # other HTML templates to render
]

DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = 5
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DISPLAY_CATEGORIES_ON_MENU = True
TYPOGRIFY = True
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
