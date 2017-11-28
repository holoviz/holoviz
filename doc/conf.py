# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = u'pyviz'
authors = u'pyviz'
copyright = u'2017 ' + authors
description = 'How to solve visualization problems with Python tools.'

# TODO: gah, version
version = '0.0.1'
release = '0.0.1'

html_static_path += ['_static']
html_theme = 'sphinx_ioam_theme'
html_theme_options = {
    'logo':'pyviz-logo.png',
    'favicon':'favicon.ico'
#    'css':'pyviz.css'
}

_NAV =  (
    ('Tutorial', 'tutorial/index'),
    ('FAQ', 'FAQ'),
    ('About', 'about')
)

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    # will work without this - for canonical (so can ignore when building locally or test deploying)    
    'WEBSITE_SERVER': 'https://pyviz.github.io/pyviz',
    'VERSION': version,
    'NAV': _NAV,
    'LINKS': _NAV,
    'SOCIAL': (
        ('Gitter', '//gitter.im/ioam/holoviews'),
        ('Twitter', '//twitter.com/holoviews'),
        ('Github', '//github.com/ioam/holoviews'),
    )
})
