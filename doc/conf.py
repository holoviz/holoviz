# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = u"HoloViz"
authors = u'HoloViz authors'
copyright = u'\u00a9 2017-2019, ' + authors
description = 'High-level tools to simplify visualization in Python.'

import holoviz
version = release = holoviz.__version__

html_static_path += ['_static']
html_theme = 'sphinx_holoviz_theme'
html_theme_options = {
    'logo': 'holoviz-logo.svg',
    'favicon': 'favicon.ico',
    'custom_css': 'custom.css',
    'primary_color': '#8ba0b9',
    'primary_color_dark': '#3e5e82',
    'secondary_color': '#d5dde7',
}

_NAV =  (
    ('Installation', 'installation'),
    ('Talks', 'talks/index'),
    ('Tutorial', 'tutorial/index'),
    ('Topics', 'topics/index'),
    ('FAQ', 'FAQ'),
    ('About', 'about'),
    ('Community', 'community'),
)

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    # WEBSITE_SERVER is optional for tests and local builds, but allows defining a canonical URL for search engines
    'WEBSITE_SERVER': 'http://holoviz.org',
    'VERSION': version,
    'GOOGLE_ANALYTICS_UA': 'UA-154795830-10',
    'NAV': _NAV,
    'LINKS': _NAV,
    'SOCIAL': (
        ('Gitter', '//gitter.im/pyviz/pyviz'),
        ('Github', '//github.com/holoviz/holoviz'),
    )
})
