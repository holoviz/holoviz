# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

#project = u'PyViz'
project = u"HoloVix"
authors = u'HoloViz authors'
copyright = u'\u00a9 2017-2019, ' + authors
description = 'High-level tools to simplify visualization in Python.'

import holoviz
version = release = holoviz.__version__

html_static_path += ['_static']
html_theme = 'sphinx_pyviz_theme'
html_theme_options = {
    'logo': 'pyviz-logo.png',
    'favicon': 'favicon.ico',
    'custom_css': 'custom.css',
    'primary_color': '#3c7cb0',
    'primary_color_dark': '#1f405b',
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
    'NAV': _NAV,
    'LINKS': _NAV,
    'SOCIAL': (
        ('Gitter', '//gitter.im/pyviz/pyviz'),
        ('Github', '//github.com/pyviz/holoviz'),
    )
})
