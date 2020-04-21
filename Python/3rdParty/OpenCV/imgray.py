#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function

import sys
import cv2 as cv


def convert_to_gray(input_fn, output_fn):
    original = cv.imread(input_fn)
    grayed = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
    cv.imwrite(output_fn, grayed)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        convert_to_gray(sys.argv[1], sys.argv[2])
    else:
        print("Usage: {0} <input_filename> <output_filename>".format(sys.argv[0]))

# EOF
