#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pikepdf import Pdf, Page
from argparse import ArgumentParser

def get_pages_dimensions(input_filename):
    with Pdf.open(input_filename) as pdf:
        all_dimensions = set()
        for page in pdf.pages:
            mediabox = tuple(Page(page).mediabox)
            width = mediabox[2] - mediabox[0]
            height = mediabox[3] - mediabox[1]
            all_dimensions.add((width, height))
        return all_dimensions

if __name__ == '__main__':
    parser = ArgumentParser(description='enumerates common dimensions from all pages')
    parser.add_argument('-i', '--input-filename', required=True,
        help='is the filename of the input pdf file')
    args = parser.parse_args()
    print('File "{}" has following dimensions:'.format(args.input_filename))
    for dims in get_pages_dimensions(args.input_filename):
        print(' * {0}x{1}'.format(dims[0], dims[1]))

# EOF