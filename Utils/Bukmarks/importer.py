#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2021, Antonio Alvarado Hernández

from pathlib import Path


def read_netscape_bookmarks(filename):
    with open(filename, encoding="utf-8") as stream:
        for line in [ _.strip() for _ in stream ]:
            print(line)


if __name__ == "__main__":
    testfile = Path(r"~/Downloads/bookmarks.html").expanduser()
    read_netscape_bookmarks(testfile)

# EOF
