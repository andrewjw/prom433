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

import os
import unittest

from prom433 import get_arguments, InvalidArguments


class TestArguments(unittest.TestCase):
    def setUp(self):
        os.environ = {}

    def test_user_environ(self):
        os.environ["MQTT_HOST"] = "mqtthost"
        args = get_arguments([])
        self.assertEqual("mqtthost", args.mqtt)

    def test_mqtt(self):
        args = get_arguments(["--mqtt", "mqtthost"])
        self.assertEqual("mqtthost", args.mqtt)

    def test_bind_without_port(self):
        args = get_arguments(["--bind", "192.168.1.2"])
        self.assertEqual("192.168.1.2", args.bind[0])
        self.assertEqual(9100, args.bind[1])
