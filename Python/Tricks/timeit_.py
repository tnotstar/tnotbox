#/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


def timeit_with_string():
    print("> Timing it from a string of code...")
    code = r"""
sum = 0
for i in range(100):
    sum += i
"""
    print("< Finished: {:.3f}s of total time spent!".format(timeit.timeit(code)))


def timeit_with_function():
    print("> Timing it from a function of code...")
    def code():
        sum = 0
        for i in range(100):
            sum += i
    print("< Finished: {:.3f}s of total time spent!".format(timeit.timeit(code)))


if __name__ == "__main__":
    timeit_with_string()
    timeit_with_function()

# EOF