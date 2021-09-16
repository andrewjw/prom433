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

import io
import os
import unittest

from prom433 import prometheus, get_metrics, child_process
from prom433.prometheus import METRICS

MESSAGE_TEXT = open("tests/output_sample.txt", "rb").read().decode("utf8")


def mock_popen(args, stdout):
    return MockPopenReturn(io.StringIO(MESSAGE_TEXT))


class MockPopenReturn:
    def __init__(self, buffer):
        self.stdout = buffer


class TestPrometheus(unittest.TestCase):
    def test_prometheus(self):
        child_process.rtl433([], prometheus, _popen=mock_popen)

        prom = get_metrics()
        print(prom)

        self.assertIn(
            """nexus_temperature{id="147", channel="1"} 23.100000""", prom)
        self.assertIn(
            """weather_temperature{id="250"} 16.000000""", prom)
