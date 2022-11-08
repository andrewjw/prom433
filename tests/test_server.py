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
import json
from datetime import datetime, timedelta
import unittest

from prom433 import prometheus
from prom433.server import Handler

MESSAGE_TEXT = open("tests/output_sample.txt", "rb").read().decode("utf8")


def mock_popen(args, stdout):
    return MockPopenReturn(io.StringIO(MESSAGE_TEXT))


class MockPopenReturn:
    def __init__(self, buffer):
        self.stdout = buffer


class MockHandler(Handler):
    def __init__(self):
        self.wfile = io.BytesIO()
        self.requestline = "GET"
        self.client_address = ("127.0.0.1", 8000)
        self.request_version = "1.0"
        self.command = "GET"


class TestServer(unittest.TestCase):
    def test_index(self):
        handler = MockHandler()
        handler.path = "/"
        handler.do_GET()

        handler.wfile.seek(0)
        self.assertTrue("/metrics" in handler.wfile.read().decode("utf8"))

    def test_error(self):
        handler = MockHandler()
        handler.path = "/error"
        handler.do_GET()

        handler.wfile.seek(0)
        self.assertTrue("404" in handler.wfile.read().decode("utf8"))

    def test_metrics(self):
        for line in MESSAGE_TEXT.split("\n"):
            prometheus(line)

        handler = MockHandler()
        handler.path = "/metrics"
        handler.do_GET()

        handler.wfile.seek(0)
        self.assertIn(
            "prom433_temperature", handler.wfile.read().decode("utf8"))
