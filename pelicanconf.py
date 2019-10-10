#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Yashas"
SITENAME = "Yashas's Blog"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
    ("Paul's Calc Notes", "http://tutorial.math.lamar.edu/"),
    ("Pygame", "https://www.pygame.org/news"),
)

# Social widget
SOCIAL = (
    ("My Twitter", "https://twitter.com/yashaslokesh_"),
    ("My LinkedIn", "https://www.linkedin.com/in/yashaslokesh/"),
    ("My GitHub", "https://github.com/yashaslokesh"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Adding plug-ins
PLUGIN_PATHS = ["/Users/lokeshkrishnappa/Documents/GitHub/pelican-plugins"]
# Activate the render_math plugin
PLUGINS = ["render_math"]

## Add static paths
STATIC_PATHS = ["images"]  # Add images directory from inside content directory

DEFAULT_METADATA = {"status": "draft"}
