# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join("..", "..")))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import datetime
year = datetime.date.today().year
project = 'Fredeco'
copyright =  str(year)+', Raulin L. Cadet'
author = 'Raulin L. Cadet'
release = '0.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# import os
# import sys
# sys.path.insert(0, os.path.abspath('../../src')) # or "../../src

extensions = ["sphinx.ext.autodoc",  # automatically generate documentation for modules
    "sphinx.ext.napoleon",  # to read Google-style or Numpy-style docstrings
    "sphinx.ext.viewcode",  # to allow vieing the source code in the web page
    "autodocsumm",  # to generate tables of functions, attributes, methods, etc.
    "myst_parser",
    'nbsphinx',  # to use ipynb file 
    'nbsphinx_link',
   
    ]
# source_suffix = ['.rst', '.md']
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

#########################
# [build-system]
# requires = ["wheel", "setuptools", "oldest-supported-numpy"]
# build-backend = "setuptools.build_meta"
