#!/usr/bin/env python3
# -*- coding: utf-8 -*_

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("foo")
parser.add_argument("bar")

args = parser.parse_args()

# EOF