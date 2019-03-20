#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import timeit

setup_lists = r"""\
xs = [0, 1, 2, 3, 4]
ys = [9, 8, 7, 6]
"""

merge_lists = r"""\
zs = [*xs, *ys]
"""

setup_sets = r"""\
xs = {0, 1, 2, 3, 4}
ys = {9, 8, 7, 6}
"""

merge_sets = r"""\
zs = {*xs, *ys}
"""

setup_dicts = r"""\
xs = {'a': 1, 'b': 2, 'c': 3}
ys = {'x': 7, 'y': 8, 'z': 9}
"""

merge_dicts = r"""\
zs = {*xs, *ys}
"""

if __name__ == "__main__":
    print("{:0.8f}s ellapsed".format(timeit.timeit(merge_lists, setup_lists)))
    print("{:0.8f}s ellapsed".format(timeit.timeit(merge_sets, setup_sets)))
    print("{:0.8f}s ellapsed".format(timeit.timeit(merge_dicts, setup_dicts)))

# EOF