#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint as pp
import itertools as it

class DFA(object):
    def __init__(self):
        self._xt = dict()

    def add_xt(self, x, v, y):
        if not x in self._xt:
            self._xt[x] = dict()
        self._xt[x][v] = y

    def accept(self, tape):
        print("tape:", tape, "", end="")
        x = 'A'
        for v in tape:
            if not v in self._xt[x]:
                print(x)
                return False
            x = self._xt[x][v]
        print(x)
        return x == 'D'

    def count(self, length):
        counter = 0
        for t in ["".join(v) for v in it.product('01', repeat=length)]:
            if self.accept(t):
                counter += 1
        return counter

    def __str__(self):
        return pp.pformat(self._xt)

if __name__ == '__main__':
    dfa = DFA()
    x = """
    dfa.add_xt('A', '0', 'B')
    dfa.add_xt('A', '1', 'C')
    dfa.add_xt('B', '1', 'D')
    dfa.add_xt('C', '0', 'D')
    dfa.add_xt('D', '0', 'A')
    dfa.add_xt('D', '1', 'B')
    print(dfa)
    print("---------")
    dfa.accept("101111")
    dfa.accept("011")
    print("---------")
    for n in range(0):
        print(dfa.count(n))
        print("---------")
    """
    dfa.add_xt('A', '0', 'B')
    dfa.add_xt('A', '1', 'C')
    dfa.add_xt('B', '1', 'D')
    dfa.add_xt('C', '0', 'D')
    dfa.add_xt('D', '0', 'A')
    dfa.add_xt('D', '1', 'B')
    print(dfa)
    print("---------")
    dfa.accept("100")
    dfa.accept("10001")
    dfa.accept("100011")
    dfa.accept("01011")
    print("---------")
    print(dfa.count(11))
    print(dfa.count(12))
    print(dfa.count(13))

# EOF
