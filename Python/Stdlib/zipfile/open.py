#!/usr/bin/env python3
# -*- coding: utf-8

from zipfile import ZipFile

with ZipFile("example.zip") as zip:
    with zip.open("example1.txt") as input:
        for line in input:
            print(line.decode())

# EOF