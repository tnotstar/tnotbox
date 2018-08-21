#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask


webapp = Flask(__name__)

@webapp.route("/")
def home():
    return "Hello, world!"


if __name__ == "__main__":
    webapp.run()

# EOF
