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

from prom433 import prometheus, get_metrics
from prom433.prometheus import METRICS

MESSAGE_TEXT = open("tests/output_sample.txt", "rb").read().decode("utf8")


def mock_popen(args, stdout):
    return MockPopenReturn(io.StringIO(MESSAGE_TEXT))


class MockPopenReturn:
    def __init__(self, buffer):
        self.stdout = buffer


class TestPrometheus(unittest.TestCase):
    def test_prometheus(self):
        for line in MESSAGE_TEXT.split("\n"):
            prometheus(line)

        prom = get_metrics()
        print(prom)

        self.assertIn(
            """prom433_temperature{channel="1", id="147\"""" +
            """, model="Nexus-TH"} 23.100000""", prom)
        self.assertIn(
            """prom433_temperature{id="250", """ +
            """model="Fineoffset-WHx080"} 16.000000""",
            prom)
        self.assertIn(
            """prom433_temperature{channel="2", id="1940", """ +
            """model="Eurochron-EFTH800"} 22.300000""", prom)
        self.assertIn(
            """prom433_noise{channel="6", id="3672", """ +
            """model="Eurochron-EFTH800"} -20.3544""", prom)
