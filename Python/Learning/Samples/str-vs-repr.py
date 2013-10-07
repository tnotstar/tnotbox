#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Test(object):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __str__(self):
        return "An instance of class Test with state: a=%s b=%s" % (self._a, self._b)

    def __repr__(self):
        return 'Test("%s","%s")' % (self._a, self._b)

if __name__ == '__main__':
    x = Test('hello', 'world')
    print 'Human readable: ', str(x)
    print 'Object representation: ', repr(x)
    print

    y = eval(repr(x))
    print 'Human readable: ', str(y)
    print 'Object representation: ', repr(y)
    print

# EOF