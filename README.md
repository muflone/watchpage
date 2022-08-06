# WatchPage
[![Travis CI Build Status](https://img.shields.io/travis/com/muflone/watchpage/master.svg)](https://www.travis-ci.com/github/muflone/watchpage)
[![CircleCI Build Status](https://img.shields.io/circleci/project/github/muflone/watchpage/master.svg)](https://circleci.com/gh/muflone/watchpage)
[![PyPI - Version](https://img.shields.io/pypi/v/WatchPage.svg)](https://pypi.org/project/WatchPage/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/WatchPage.svg)](https://pypi.org/project/WatchPage/)

**Description:** Watch webpages for changes

**Copyright:** 2022 Fabio Castelli (Muflone) <muflone@muflone.com>

**License:** GPL-3+

**Source code:** https://github.com/muflone/watchpage

**Documentation:** http://www.muflone.com/watchpage/

# Description

WatchPage is a simple tool to watch multiple web pages for changes.

It aims to ease the software maintainers to check for changes to the project
sites and get any news based on patterns.

# System Requirements

* Python 3.x
* PyYAML 6.0 (https://pypi.org/project/PyYAML/)
* BeautifulSoup4 4.x (https://pypi.org/project/beautifulsoup4/)
* lxml 4.9 (https://pypi.org/project/lxml/)
* html5lib 1.1 (https://pypi.org/project/html5lib/)

# Usage

WatchPage is a command line utility and it requires some arguments to be passed:

`watchpage --config <CONFIGURATION> --results <RESULTS> [--dump]`

The argument `--config` refers to a valid YAML configuration file
(see below for some examples).

The argument `--results` must be the path to a directory where to save the
results files.

The argument `--dump` will show the results but it will discard the changes, so
they will not be saved in the directory specified in the `--results` argument.

An example to execute WatchPage will be the following:

`watchpage --config docs/muflone_apps.yaml --results output`

All the targets specified in the configuration file `muflone_apps.yaml` will be
processed, results will be saved in the `output` directory and the differences
will be printed in the stdout.
