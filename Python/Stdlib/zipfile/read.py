#!/usr/bin/env python3
# -*- coding: utf-8

from zipfile import ZipFile

with ZipFile("example.zip") as zip:
    buffer = zip.read("spanish/example2.txt")
    print(buffer.decode())

# EOF