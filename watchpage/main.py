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

from watchpage.command_line_options import CommandLineOptions
from watchpage.configuration import Configuration


def main():
    # Get command-line options
    command_line = CommandLineOptions()
    command_line.add_configuration_arguments()
    options = command_line.parse_options()
    configuration = Configuration(options.config)
    for target in configuration.get_targets():
        results = target.get_results()
        print(target.name, results)


if __name__ == '__main__':
    main()
