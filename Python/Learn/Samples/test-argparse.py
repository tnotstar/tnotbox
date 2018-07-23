#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

def test_minimal():
    parser = ArgumentParser()
    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    test_minimal()

# EOF