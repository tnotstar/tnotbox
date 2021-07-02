#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pikepdf import Name, open as open_pdf
from argparse import ArgumentParser

def get_pages_dimensions(input_filename):
    with open_pdf(input_filename) as pdf:
        index = 0
        all_dimensions = dict()
        for page in pdf.pages:
            if Name.CropBox in page:
                box = tuple(page.CropBox)
            else:
                box = tuple(page.MediaBox)
            width = round(2.54*float(box[2] - box[0])/72.0, 2)
            height = round(2.54*float(box[3] - box[1])/72.0, 2)
            index += 1
            if (width, height) in all_dimensions:
                all_dimensions[(width, height)].append(index)
            else:
                all_dimensions[(width, height)] = [ index ]
        return all_dimensions

if __name__ == '__main__':
    parser = ArgumentParser(description='enumerates common dimensions from all pages')
    parser.add_argument('-i', '--input-filename', required=True,
        help='is the filename of the input pdf file')
    args = parser.parse_args()
    print('File "{}" has following dimensions:'.format(args.input_filename))
    for dimensions in get_pages_dimensions(args.input_filename):
        print(' * {0} x {1}'.format(dimensions[0], dimensions[1]))

# EOF