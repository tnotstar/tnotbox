# -*- coding: utf-8 -*-
#
# Copyright (c) 2014, Antonio Alvarado Hernández and contributors
# All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#



from __future__ import absolute_import, unicode_literals

import unittest
import threading

from scrapes import WebAgent
from scrapes.compat import BaseClass, HTTPServer, BaseHTTPRequestHandler


class FakeRequestHandler(BaseHTTPRequestHandler, BaseClass):
    """Blah, blah, blah, ...

    Original code borrowed from https://code.google.com/p/feedparser/
    """

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Hello, world!\n")


class FakeHTTPServer(threading.Thread, BaseClass):
    """Blah, blah, blah, ...

    Original code borrowed from https://code.google.com/p/feedparser/
    """

    def __init__(self, requests=1):
        super(FakeHTTPServer, self).__init__()
        self._requests = requests
        self._server = HTTPServer(("localhost", 9999), FakeRequestHandler)
        self._ready = threading.Event()

    def run(self):
        print "Setting ready event..."
        self._ready.set()
        while self._requests:
            print "Serving a requets..."
            self._server.handle_request()
            self._requests -= 1
            print "Nr. requests after decrement: ", self._requests
        print "Clearing ready event..."
        self._ready.clear()


class TestWebAgent(unittest.TestCase):
    """Blah, blah, blah, ..."""

    def setUp(self):
        print "setting up..."
        self._websrv = FakeHTTPServer()
        self._websrv.start()

    def tearDown(self):
        print "tearing down..."
        #self._websrv._ready.wait()

    def test_example(self):
        agent = WebAgent()
        agent.get("http://localhost:9999")

# EOF
