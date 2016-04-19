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
    'Nature': {
        'description': "That what's you miss less when you miss it most.",
        'thumbnail': 'http://thumbs.dreamstime.com/x/logo-de-nature-7533173.jpg'
    },
    'Coding': {
        'description': 'You type a few lines and sometimes it works.',
        'thumbnail': 'https://tctechcrunch2011.files.wordpress.com/2015/04/codecode.jpg'
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
            Nature is my home. Outdoors, mindfulness, challenges. I can speak French.
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
