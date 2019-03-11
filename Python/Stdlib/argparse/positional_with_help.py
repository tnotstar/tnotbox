#!/usr/bin/env python3
# -*- coding: utf-8 -*_

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("foo", help="one argument")
parser.add_argument("bar", help="bar argument")

args = parser.parse_args()

# EOF