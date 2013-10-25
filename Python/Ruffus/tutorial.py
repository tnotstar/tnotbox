#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from ruffus import *

def first_task():
    print("Hello,")

@follows(first_task)
def second_task():
    print("world!")

if __name__ == '__main__':
    pipeline_run([second_task], verbose = 1)

# EOF