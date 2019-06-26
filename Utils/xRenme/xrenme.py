#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from pathlib import Path


DEFAULT_GLOB_PATTERN = "*"

def main():
    parser = build_argument_parser()
    args = parser.parse_args()
    print("1> args = {}".format(args))
    if not args.input_list or args.input_list == "-":
        args.input_list = "hello.txt"
    if not args.glob_pattern:
        args.glob_pattern = "*"
    print("2> args = {}".format(args))


def build_argument_parser():
    """Return a new and configurated argument parser"""
    description="A simple tool to batch rename given files."
    parser = ArgumentParser(description=description)
    parser.add_argument("-i", "--input-list", required=False,
        help="the path to the input list file.")
    parser.add_argument("-p", "--glob-pattern", default=DEFAULT_GLOB_PATTERN,
        help="a glob pattern to filter input files.")
    return parser


if __name__ == "__main__":
    main()

# EOF