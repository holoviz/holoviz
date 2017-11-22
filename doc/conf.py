# -*- coding: utf-8 -*-


from nbsite.shared_conf import * # noqa

##############################################################
# start of things to edit

project = u'anacondaviz'
authors = u'anacondaviz'
copyright = u'2017 ' + authors

# TODO: rename
ioam_module = 'anacondaviz'
description = 'How to solve visualization problems with Python tools.'

# TODO: gah, version
version = '0.0.1'
release = '0.0.1'

html_static_path = ['_static']

html_theme = 'sphinx_ioam_theme'
html_theme_options = {
#    'logo':'images/amazinglogo.png'
#    'favicon':'images/amazingfavicon.ico'
# ...
# ? css
# ? js
}


_NAV =  (
        ('Tutorial', 'tutorial/index'),
#        ('User Guide', 'user_guide/index'),
#        ('Gallery', 'gallery/index'),
#        ('API', 'Reference_Manual/index'),
        ('FAQ', 'FAQ'),
        ('About', 'about'))

html_context = {
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    # will work without this - for canonical (so can ignore when building locally or test deploying)    
    'WEBSITE_SERVER': 'https://continuumio.github.io/anacondaviz',
    'VERSION': version,
    'NAV': _NAV,
    'LINKS': _NAV,
    'SOCIAL': (
        ('Gitter', '//gitter.im/ioam/holoviews'),
        ('Twitter', '//twitter.com/holoviews'),
        ('Github', '//github.com/ioam/holoviews'),
    ),
    'js_includes': ['custom.js', 'require.js'],
}

# end of things to edit
##############################################################

from nbsite.shared_conf2 import hack
setup, intersphinx_mapping, texinfo_documents, man_pages, latex_documents, htmlhelp_basename, html_static_path, html_title, exclude_patterns = hack(project,ioam_module,authors,description,html_static_path)
