#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

JINJA_EXTENSIONS = ['jinja2.ext.loopcontrols']

AUTHOR = 'sta'
SITENAME = 'BALab'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = 'Greek'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None
#LINKS = (('Github repository', 'http://github.org/nlp-unibuc'),
#        ('Vlad Niculae', 'http://vene.ro'))

# Social widget
SOCIAL = ()

# Plugins
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['pelican-bibtex']
PUBLICATIONS_SRC = 'content/pubs.bib'

THEME = 'theme'

DIRECT_TEMPLATES = ('publications','index')

DEFAULT_PAGINATION = False

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (
    ('Publications', 'publications.html'),
)

# directories to be copied into output/static/
STATIC_PATHS = ['img', 'css', 'js']
# very useful for debugging purposes
DELETE_OUTPUT_DIRECTORY = True
RELATIVE_URLS = True
