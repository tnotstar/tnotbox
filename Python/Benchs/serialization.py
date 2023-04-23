#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint as pp

import pickle
import timeit
import functools


def generate_data(width, depth, pattern, count):
    data = dict()
    for w in range(width):
        key = "attribute{0:2d}".format(w)
        if depth > 0:
            data[key] = generate_data(width, depth - 1, pattern, count)
        else:
            data[key] = count * pattern
    return data


def pickle_serialize(data):
    """Serialize given data structure in memory"""
    pickle.dumps(data)


def pickle_unserialize(data):
    """Unserialize given data structure in memory"""
    return pickle.loads(data)


if __name__ == "__main__":
    environ = dict()
    width = 10
    depth = 3
    pattern = "-oIo-"
    count = 10
    number = 500
    data = generate_data(width, depth, pattern, count)
    undata = pickle.dumps(data)

    print("{0}: {1}s".format(pickle_serialize.__doc__,
        min(timeit.Timer(stmt=functools.partial(pickle_serialize, data)).
            repeat(5, number)
        )/number
    ))

    print("{0}: {1}s".format(pickle_unserialize.__doc__,
        min(timeit.Timer(stmt=functools.partial(pickle_unserialize, undata)).
            repeat(5, number)
        )/number
    ))

# EOF
