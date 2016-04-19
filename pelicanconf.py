#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'admin'
SITENAME = u'Plural Parallel'
SITEURL = ''
LOAD_CONTENT_CACHE = False

PATH = 'content'
STATIC_PATHS = ['images']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DISQUS_SITENAME = "pluralparallel"
GOOGLE_ANALYTICS= "UA-76598222-1"
THEME = 'medius'
MEDIUS_CATEGORIES = {
    'Review': {
        'description': 'A galaxy is a gravitationally bound system of stars, stellar remnants, interstellar gas and dust, and dark matter.',
        'logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/GalacticRotation2.svg/250px-GalacticRotation2.svg.png',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/NGC_3923_Elliptical_Shell_Galaxy.jpg/220px-NGC_3923_Elliptical_Shell_Galaxy.jpg'
    }
}
MEDIUS_AUTHORS = {
    'chris': {
        'description': """
            My geeky skills somehow allow to maintain this website for me and my pals.
        """,
        'cover': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Milky_Way_Arch.jpg/1920px-Milky_Way_Arch.jpg',
        'image': 'https://lh6.googleusercontent.com/-zEMaXmWAhdI/AAAAAAAAAAI/AAAAAAAAAAA/eVdgsm3TIDU/s128-c-k/photo.jpg',
    },
    'helmut': {
        'description': """
            Nature is my home. Outdoors, mindfulness, challenges.
        """,
        'cover': '/images/climbersfingers.jpg',
        'image': 'https://lh6.googleusercontent.com/-zEMaXmWAhdI/AAAAAAAAAAI/AAAAAAAAAAA/eVdgsm3TIDU/s128-c-k/photo.jpg',
    },
    'edgar': {
        'description': """
            Humans come and go.
        """,
        'cover': '/images/climbersfingers.jpg',
        'image': 'https://lh6.googleusercontent.com/-zEMaXmWAhdI/AAAAAAAAAAI/AAAAAAAAAAA/eVdgsm3TIDU/s128-c-k/photo.jpg',
    },
    'pichan': {
        'description': """
            How deep are your roots ?
        """,
        'cover': '/images/climbersfingers.jpg',
        'image': 'https://lh6.googleusercontent.com/-zEMaXmWAhdI/AAAAAAAAAAI/AAAAAAAAAAA/eVdgsm3TIDU/s128-c-k/photo.jpg',
    },
    'bottle': {
        'description': """
             Noumenon enthusiast.
        """,
        'cover': '/images/climbersfingers.jpg',
        'image': 'https://lh6.googleusercontent.com/-zEMaXmWAhdI/AAAAAAAAAAI/AAAAAAAAAAA/eVdgsm3TIDU/s128-c-k/photo.jpg',
    },
}
