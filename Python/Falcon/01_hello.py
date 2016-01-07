#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref import simple_server

import falcon


class HelloResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Hello, world!\n"

api = falcon.API()
api.add_route("/hello", HelloResource())

if __name__ == '__main__':
    http = simple_server.make_server('127.0.0.1', 8080, api)
    http.serve_forever()

# EOF
