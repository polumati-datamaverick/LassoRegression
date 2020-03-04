import io

import os

from pathlib import Path

from setuptools import find_packages, setup

#Package meta-data

NAME = 'regression_model'
DESCRIPTION = 'Train and deploy regression model'
URL = 'Git hub location'
EMAIL = 'satish.datamaverick@gmail.com'
AUTHOR = 'Your Name'
REQUIRES_PYTHON = '>=3.6.0'


# What packages are required for this module to be executed?
def list_reqs(fname = 'requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()


here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'),encoding = 'utf-8') as f:
        long_description = '\n'+f.read()

except FileNotFoundError:
    long_description = DESCRIPTION

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}

with open (PACKAGE_DIR / 'VERSION') as f:

    _version = f.read().strip()
    about['__version__'] = _version


setup (
    name = NAME,
    version = about['__version__'],
    description = DESCRIPTION,
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = AUTHOR,
    author_email = EMAIL,
    python_requires = REQUIRES_PYTHON,
    url = URL,
    packages = find_packages(exclude=('tests',)),
    package_data = {'regreaaion_model':['VERSION']},
    install_requires = list_reqs(),
    extras_require = {},
    include_package_data = True,
    classifier = [
        # Trove classifiers
        # Full list : https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License ',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'

    ]

)





