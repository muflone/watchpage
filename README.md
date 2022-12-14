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

Launching again the previous command you **will not** get any results as there
will not be further changes after the previous run.
The saved items will be stored in the directory specified in the `results`
argument.

Adding `--dump` you can observe the returned values but the changes will not be
saved.

# Configuration file

A configuration file is a YAML specification file with the following values:

- `NAME`: a unique string to identify the target to process
- `URL`: the page URL to monitor for changes
- `PARSER`: the parser to use to process the URL. This can be either:
  - `html.parser`: this will use the default Python HTML parser
  - `html5`: this will use [html5lib](https://pypi.org/project/html5lib/) to
    process the page
  - `lxml`: this will use [lxml](https://lxml.de/) HTML parser
  - `xml`: this will use [lxml](https://lxml.de/) XML parser
- `TYPE`: specify the type of items to process from the page. This value can be:
  - `links`: will get all the anchors from a HTML page
  - `rss`: will get all the link items from a RSS feed
  - `text`: will process the page as a simple text file
- `ABSOLUTE_URLS`: a boolean value (true/false) to make the processed URLs as
  absolute by appending the website from the URL page
- `FILTERS`: a list of filters to apply to find the matched items. This can be
  any of the following:
  - `STARTS`: the item must begin with the specified string
  - `NOT STARTS`: the item must not begin with the specified string
  - `ENDS`: the item must end with the specified string
  - `NOT ENDS`: the item must not end with the specified string
  - `CONTAINS`: the item must contain the specified string
  - `NOT CONTAINS`: the item must not contain the specified string
  - `REGEX`: the item must match the specified regular expression string
  - `NOT REGEX`: the item must not match the specified regular expression string
- `STATUS`: a boolean value (true/false) to enable or disable the target

# Configuration example files

Some configuration example files can be found in the `docs` directory.

```yaml
NAME: gnome-appfolders-manager
URL: https://github.com/muflone/gnome-appfolders-manager/tags
PARSER: html5
TYPE: links
ABSOLUTE_URLS: true
FILTERS:
  - STARTS: https://github.com/muflone/
  - ENDS: .tar.gz
STATUS: true
```

This configuration file will use the html5 parser to scan all the links in the
page that begin with https://github.com/muflone/ and ending with .tar.gz

---
```yaml
NAME: dbeaver_plugins
URL: https://dbeaver.io/update/ce/latest/plugins/
PARSER: html.parser
TYPE: text
FILTERS:
  - CONTAINS: .jar
STATUS: false
```

This configuration file will use the html parser to scan all the lines in the
page containing the text .jar

---
```yaml
NAME: gmtp
URL: https://sourceforge.net/projects/gmtp/rss
PARSER: xml
TYPE: rss
FILTERS:
  - ENDS: .tar.gz/download
STATUS: true
```

This configuration file will use the xml parser to scan all the links in the
RSS feed ending with .tar.gz/download
