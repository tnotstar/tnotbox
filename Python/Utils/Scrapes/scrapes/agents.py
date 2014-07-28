# -*- coding: utf-8 -*-
#
# Copyright 2014 Antonio Alvarado Hernández
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

from requests import Session


class Itzamna(object):
    """Blah, blah, blah, ..."""

    def __init__(self, config=None):
        self._config = config
        self._session = Session()

    @property
    def config(self):
        return self._config

    def get(self, url):
        """Blah, blah, blah, ..."""
        try:
            response = self._session.get(url)
            print response
        except Exception as ex:
            print "oops", str(ex)

# EOF
