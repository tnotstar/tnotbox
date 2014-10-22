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
from scrapes.compat import BaseHTTPServer as httpsrv



class MockWebServer(object):
    """Blah, blah, blah, ..."""

    class RequestHandler(httpsrv.BaseHTTPRequestHandler):
        """Blah, blah, blah, ..."""

        server_version = "MockWebServer/0.1"

        def do_GET(self):
            """Blah, blah, blah, ..."""
            if self.path in self.server.requests_map:
                response = self.server.requests_map.get(self.path)
                mimetype = response.get("mimetype")
                content = response.get("content")
                length = len(content)
                self.send_response(200)
                self.send_header("Content-Type", mimetype)
                self.send_header("Content-Length", str(length))
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_response(500)
                self.end_headers()

    def __init__(self, requests_map, server_host=None, server_port=9999):
        """Blah, blah, blah, ..."""
        server_address = (server_host or "", server_port)
        request_handler = self.RequestHandler
        self._server = httpsrv.HTTPServer(server_address, request_handler)
        self._server.requests_map = requests_map
        self._thread = threading.Thread(target=self._run_server)

    def _run_server(self, *args, **kwargs):
        """Blah, blah, blah, ..."""
        print("Now, server is running...")
        self._server.serve_forever()
        print("Now, server is shutting down...")

    def start(self):
        """Blah, blah, blah, ..."""
        self._thread.start()

    def stop(self):
        """Blah, blah, blah, ..."""
        self._server.shutdown()
        self._thread.join()


class TestWebAgent(unittest.TestCase):
    """Blah, blah, blah, ..."""

    requests_map = {
        "/": {"mimetype": "text/plain",
              "content":  "Hello, world!"},
    }

    def setUp(self):
        print "setting up..."
        self._websrv = MockWebServer(self.requests_map, "localhost", 9999)
        self._websrv.start()

    def tearDown(self):
        print "tearing down..."
        self._websrv.stop()
        print "finished!"

    def test_example(self):
        agent = WebAgent()
        agent.get("http://localhost:9999/")

# EOF
