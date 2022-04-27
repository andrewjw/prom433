# prom433
# Copyright (C) 2021 Andrew Wilkinson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import os

parser = argparse.ArgumentParser(
    description='Listens to messages from rtl_433 and exposes them '
    + 'as prometheus metrics')
parser.add_argument('--bind', type=str, nargs='?', default="0.0.0.0:9100",
                    help='the ip address and port to bind to')
parser.add_argument('--mqtt', type=str, nargs='?', default="mqtt",
                    help="the mqtt host to connect to")


def get_arguments(args):
    args = parser.parse_args(args)
    if "MQTT_HOST" in os.environ:
        args.mqtt = os.environ["MQTT_HOST"]

    if ":" not in args.bind:
        args.bind = (args.bind, 9100)
    else:
        args.bind = (args.bind.split(":")[0], int(args.bind.split(":")[1]))

    return args
