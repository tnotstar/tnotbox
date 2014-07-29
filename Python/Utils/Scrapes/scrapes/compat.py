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

from six import (PY2, PY3)
from six.moves.BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


class BaseClass(object):
    """A mixin class to fix some compatibility issues."""

    def __repr__(self):
        result = self.__str__()
        if six.PY3:
            return result
        else:
            return result.encode('utf-8')


__all__ = [
    'BaseClass',
    'BaseHTTPRequestHandler',
    'HTTPServer',
]

# EOF
