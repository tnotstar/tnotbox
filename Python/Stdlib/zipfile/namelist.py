#!/usr/bin/env python3
# -*- coding: utf-8

from zipfile import ZipFile

with ZipFile("example.zip") as zip:
    for name in zip.namelist():
        print(name)

# EOF