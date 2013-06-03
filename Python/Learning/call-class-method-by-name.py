#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CallMethodByName(object):
    def __init__(self, data):
        self._data = data

    def run(self):
        for key, value in self._data.items():
            if key in self._field_map:
                func = getattr(self, self._field_map[key])
                print key, value, func(value)

    def _from_string(self, value):
        print "Calling _from_string(" + str(value) + ")..."
        return str(value)

    def _from_integer(self, value):
        print "Calling _from_integer(" + str(value) + ")..."
        return str(value)

    _field_map = {
        'name': '_from_string',
        'age':  '_from_integer',
    }

if __name__ == '__main__':
    o = CallMethodByName({'name': 'joe', 'age': 33})
    o.run()

# EOF