#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import array
import timeit
import functools


def repstr1(value, count):
    """Repeat given string using string concatenation"""
    buffer = str()
    for i in range(count):
        buffer += value
    return buffer


def repstr2(value, count):
    """Repeat given string using and array of unicode values"""
    buffer = array.array("b")
    value = value.encode()
    for i in range(count):
        buffer.frombytes(value)
    return buffer.tobytes().decode("utf-8")


def repstr3(value, count):
    """Repeat given string using an StringIO"""
    buffer = io.StringIO()
    for i in range(count):
        buffer.write(value)
    return buffer.getvalue()


def repstr4(value, count):
    """Repeat given string using a list and then join with \"\""""
    buffer = list()
    for i in range(count):
        buffer.append(value)
    return "".join(buffer)


if __name__ == "__main__":
    pattern = "-*-"
    counts = 1000
    repeats = 25000
    print("{0}: {1}s".format(repstr1.__doc__, timeit.timeit(stmt=functools.partial(
        repstr1, pattern, counts), number=repeats)))
    print("{0}: {1}s".format(repstr2.__doc__, timeit.timeit(stmt=functools.partial(
        repstr2, pattern, counts), number=repeats)))
    print("{0}: {1}s".format(repstr3.__doc__, timeit.timeit(stmt=functools.partial(
        repstr3, pattern, counts), number=repeats)))
    print("{0}: {1}s".format(repstr4.__doc__, timeit.timeit(stmt=functools.partial(
        repstr4, pattern, counts), number=repeats)))

# EOF
