#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Evgeny Pogorelov'
SITENAME = AUTHOR
SITEURL = 'localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = 'Side projects and writings'
SITEDESCRIPTION = "Side projects and writings"
SITELOGO = SITEURL + '/images/profile.jpeg'
FAVICON = SITEURL + '/images/favicon.ico'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2022

THEME = "./themes/Flex/"
PATH = 'content'
TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/evgenypogorelov/en'),
          ('github', 'https://github.com/pogoetic'),
          ('twitter', 'https://twitter.com/pogoetic'),
          ('rss', '//pogoetic.github.io/feeds/all.atom.xml'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

#LINKS = (('about', 'http://evgenypogorelov.com'),)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

#PLUGIN_PATHS = ['./plugins']

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup, 'sitemap']


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

EXTRA_PATH_METADATA = {
    #'extra/custom.css': {'path': 'static/custom.css'},
    'extra/CNAME': {'path': 'CNAME'}
}
#CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True

STATIC_PATHS = ['images', 'extra']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]  

DISQUS_SITENAME = 'evgenysblog-1'
GOOGLE_ANALYTICS = "G-DT82FP28W3"
#GOOGLE_TAG_MANAGER = "GTM-WBFQQB6"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True