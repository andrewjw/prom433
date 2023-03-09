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
DROP_TEXT = open("tests/dropmetric_sample.txt", "rb").read().decode("utf8")
TIMESTAMP_TEXT = open("tests/timestamp_sample.txt", "rb").read().decode("utf8")


def mock_popen(args, stdout):
    return MockPopenReturn(io.StringIO(MESSAGE_TEXT))


class MockPopenReturn:
    def __init__(self, buffer):
        self.stdout = buffer


class TestPrometheus(unittest.TestCase):
    def test_prometheus(self):
        for line in MESSAGE_TEXT.split("\n"):
            prometheus(line, 0)

        prom = get_metrics()

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
        self.assertIn(
            """prom433_radio_clock{channel="2", id="1940", """ +
            """model="Eurochron-EFTH800"} 1670453240.000000""", prom)

    def test_drop_metric_after(self):
        for line in DROP_TEXT.split("\n"):
            prometheus(line, 3600)

        prom = get_metrics()

        # The Nexus wasn't dropped because it was updated 30 minutes ago,
        self.assertIn("""Nexus-TH""", prom)
        # The Eurochron message was the one that triggered the delete...
        self.assertIn("""Eurochron-EFTH800""", prom)
        # but the Fineoffset hasn't been seen for an hour, so was dropped.
        self.assertNotIn("""Fineoffset-WHx080""", prom)

    def test_drop_metric_disabled(self):
        for line in DROP_TEXT.split("\n"):
            prometheus(line, 0)

        prom = get_metrics()

        # The Nexus wasn't dropped because it was updated 30 minutes ago,
        self.assertIn("""Nexus-TH""", prom)
        # The Eurochron message was the one that triggered the delete...
        self.assertIn("""Eurochron-EFTH800""", prom)
        # The Fineoffset hasn't been seen for an hour,
        # but dropping is disabled.
        self.assertIn("""Fineoffset-WHx080""", prom)

    def test_timestamp(self):
        for line in TIMESTAMP_TEXT.split("\n"):
            prometheus(line, 0)

        prom = get_metrics()

        # Test for time in format time:utc:tz
        self.assertIn(
            """prom433_last_message{id="1", """ +
            """model="LaCrosse-TX"} 1677374905.000000""", prom)
        # Test for time in format time:tz
        self.assertIn(
            """prom433_last_message{id="2", """ +
            """model="LaCrosse-TX"} 1677374905.000000""", prom)
        # Test for time in format time:iso:tz
        self.assertIn(
            """prom433_last_message{id="3", """ +
            """model="LaCrosse-TX"} 1677374905.000000""", prom)
        # Test for time in format time:unix
        self.assertIn(
            """prom433_last_message{id="4", """ +
            """model="LaCrosse-TX"} 1677374905.000000""", prom)
        # Test for time in format time:utc:tz:usec
        self.assertIn(
            """prom433_last_message{id="101", """ +
            """model="LaCrosse-TX31UIT"} 1677374905.538138""", prom)
        # Test for time in format time:tz:usec
        self.assertIn(
            """prom433_last_message{id="102", """ +
            """model="LaCrosse-TX31UIT"} 1677374905.538138""", prom)
        # Test for time in format time:iso:tz:usec
        self.assertIn(
            """prom433_last_message{id="103", """ +
            """model="LaCrosse-TX31UIT"} 1677374905.538138""", prom)
        # Test for time in format time:unix:usec
        self.assertIn(
            """prom433_last_message{id="104", """ +
            """model="LaCrosse-TX31UIT"} 1677374905.538138""", prom)
