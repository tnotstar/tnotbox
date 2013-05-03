#!/usr/bin/env python

from __future__ import print_function

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

server = tornado.web.Application([
    (r'/', MainHandler),
])

if __name__ == '__main__':
    print("Starting server at http://localhost:8888/ ...")
    server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

# EOF