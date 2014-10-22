#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

class NativeScanner(object):
    """TODO"""

    def __init__(self, input):
        if isinstance(input, str):
            if os.path.exists(input):
                self._input = open(input, 'rb')
            else:
                self._input = io.StringIO(input)
        else:
            self._input = input
        self._line = 0
        self._column = 0

class NativeParser(object):
    """TODO"""

    def __init__(self):
        """Initializes given parser object."""
        self._buffer = None
        self._length = 0
        self._current = 0

    def parse_file(self, filename):
        """Parses contents from file with given filename."""
        with open(filename) as stream:
            return self.parse(stream.read())

    def parse(self, buffer):
        """Parses given input buffer."""
        self._reset(buffer)
        while True:
            next = self._next()
            if not next:
                break
            print(next)
        return None

    def _reset(self, buffer):
        """TODO"""
        self._buffer = buffer
        self._length = len(self._buffer)
        self._current = 0

    def _next(self):
        """TODO"""
        self._current += 1
        if self._current <= self._length:
            return self._buffer[self._current-1:self._current]
        else:
            return None


def parse_native_file(filename):
    p = NativeParser()
    try:
        return p.parse_file(filename)
    except IOError as e:
        return None

def main():
    print("Begining...")
    output = parse_native_file("testdoc.native")
    print(output)
    print("Finished!")

if __name__ == '__main__':
    main()

# EOF