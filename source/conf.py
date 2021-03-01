# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the # documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../../'))


# -- Project information -----------------------------------------------------

project = 'Oase'
copyright = ''
author = 'Kurt & Jia'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
# extensions = ['sphinx.ext.autodoc']

autodoc_default_options = {
    # 'members': True,
    'member-order': 'groupwise',
    # 'undoc-members': False,
    'private-members': True
}

autoclass_content = 'both'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'
# html_theme = 'pyramid'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'FM_logo.jpeg'

html_theme_options = {
    "stickysidebar": "True"
}

html_copy_source = False

html4_writer = True

html_last_updated_fmt = ''

# html_compact_lists = False

html_title = 'OASE'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

master_doc = 'index'
