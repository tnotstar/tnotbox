#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pikepdf import Pdf, Name, open as open_pdf
from argparse import ArgumentParser


def remove_ep4stats_wm(output_filename, input_filename):
    with open_pdf(input_filename) as pdf:
        for page in pdf.pages:
            if Name.Annots in page:
                remove_from_page_annotations(page.Annots)
        pdf.save(output_filename)


def remove_from_page_annotations(annotations):
    to_delete = []
    for i in range(len(annotations)):
        annot = annotations[i]
        if annot.Type != Name.Annot:
            continue
        if annot.Subtype != Name.Widget:
            continue
        to_delete.append(i)
    for index in reversed(to_delete):
        del annotations[index]


if __name__ == '__main__':
    parser = ArgumentParser(description='remove ebooks for statistics watermark')
    parser.add_argument('-i', '--input-filename', required=True,
        help='is the name of the input file')
    parser.add_argument('-o', '--output-filename', required=True,
        help='is the name of the output file')
    args = parser.parse_args()
    remove_ep4stats_wm(args.output_filename, args.input_filename)

# EOF