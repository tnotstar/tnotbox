#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from bs4 import BeautifulSoup
from requests import Session


class Agent(object):
    """Blah, blah, blah, ..."""

    def __ini__(self, config=None):
        self._config = config

    @property
    def config(self):
        return self._config

class Scrape(object):
    """Blah, blah, blah, ..."""

    def __init__(self):
        self._session = Session()

    def get(self, url):
        try:
            response = self._session.get(url)
            soup = BeautifulSoup(response.text)
            print(soup.prettify())
        except Exception as ex:
            print("Oops... {}".format(str(ex)))

def testme():
    scrape = Scrape()
    scrape.get("http://www.google.com")

if __name__ == '__main__':
    testme()

# EOF
