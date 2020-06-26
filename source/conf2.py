# -*- coding: utf-8 -*-
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Sistēmas LĀCIS dokumentācija'
copyright = '2020 Ozols Grupa'
author = 'Ozols Grupa'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '2.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# If you want to have a consistent, platform independent look
# sphinxemoji_style = 'twemoji'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
#html_theme_options = {
#  "external_links": [
#      ("Github", "https://github.com/romnnn/sphinx_press_theme")
#  ]
#}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ["page_nav.css"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# The default `html_sidebars` of Press theme: ['util/searchbox.html', 'util/sidetoc.html']
#
#html_sidebars = {'**': ['util/sidetoc.html']}
# html_logo = 'https://mirrors.creativecommons.org/presskit/icons/heart.black.png'


#---sphinx-themes-----
#html_theme = 'glpi'
#html_theme = 'local_rtd_theme'
#html_theme = 'sphinx_ozols_theme'
#html_theme = 'alabaster_theme'
#html_theme = 'sphinx_press_theme'
#html_theme = 'alabaster'
html_theme = 'press'
html_theme_path = ["_themes", "_themes/sphinx_glpi_theme"]


