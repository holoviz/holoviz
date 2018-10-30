# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

#project = u'PyViz'
project = u"<b><span style='color:#4792cf;'>Py</span><span style='color:#fdca48;'>Viz</span></b>"
authors = u'PyViz authors'
copyright = u'\u00a9 2017-2018, ' + authors
description = 'How to solve visualization problems with Python tools.'

import pyviz
version = release = pyviz.__version__

html_static_path += ['_static']
html_theme = 'sphinx_ioam_theme'
html_theme_options = {
    'logo':'pyviz-logo.png',
    'favicon':'favicon.ico',
    'css':'site.css'
}

_NAV =  (
    ('Installation', 'installation'),
    ('Tutorial', 'tutorial/index'),
    ('Topics', 'topics/index'),
    ('FAQ', 'FAQ'),
    ('About', 'about')
)

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    # will work without this - for canonical (so can ignore when building locally or test deploying)
    'WEBSITE_SERVER': 'http://pyviz.org',
    'VERSION': version,
    'NAV': _NAV,
    'LINKS': _NAV,
    'SOCIAL': (
        ('Gitter', '//gitter.im/pyviz/pyviz'),
        ('Github', '//github.com/pyviz/pyviz'),
    )
})
