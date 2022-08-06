##
#     Project: WatchPage
# Description: Watch webpages for changes
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2022 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

import yaml


class Configuration(object):
    """
    Configuration object for loading the settings from a YAML file
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.targets = {}
        with open(self.filename, 'r') as file:
            self.values = {item['NAME']: item
                           for item in yaml.load_all(stream=file,
                                                     Loader=yaml.Loader)}

    def get_values(self) -> dict[str, list[dict]]:
        """
        Return the configuration values

        :return: list containing items
        """
        return self.values

    def get_type(self, name) -> str:
        """
        Get the type associated to the item with the specified name

        :param name: item name
        :return: associated type
        """
        return self.values[name]['TYPE']

    def get_filters(self, name) -> list[str]:
        """
        Get the filters associated to the item with the specified name

        :param name: item name
        :return: associated filters
        """
        return self.values[name].get('FILTERS', []) or []

    def get_url(self, name) -> str:
        """
        Get the URL associated to the item with the specified name

        :param name: item name
        :return: associated URL
        """
        return self.values[name]['URL']

    def open_url(self, name) -> str:
        """
        Get the result from the associated URL

        :param name: item name
        :return: parsed page
        """
        with urllib.request.urlopen(url=self.get_url(name=name)) as request:
            results = request.read()
        return results

    def parse_url(self, name) -> BeautifulSoup:
        """
        Parser the associated URL

        :param name: item name
        :return: parsed page
        """
        parser = self.values[name]['PARSER']
        soup = BeautifulSoup(markup=self.open_url(name=name),
                             features=parser)
        return soup

    def get_links(self, name) -> list[str]:
        """
        Get all the links in the page

        :param name: item name
        :return: list of URLs
        """
        base_url = self.get_url(name=name)
        parser = self.parse_url(name=name)
        use_absolute_urls = self.values[name]['ABSOLUTE_URLS']
        results = []
        for anchor in parser.find_all('a'):
            # Find only anchors with href
            if 'href' in anchor.attrs:
                if use_absolute_urls:
                    # Make URL absolute
                    url = urllib.parse.urljoin(base=base_url,
                                               url=anchor['href'])
                else:
                    # Leave the URL as is
                    url = anchor['href']
                results.append(url)
        return results
