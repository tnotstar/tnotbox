#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pikepdf import Pdf, Name, open as open_pdf
from argparse import ArgumentParser

import re

ITEBOOKS_RX = re.compile(b'www\.it-ebooks\.info')
ITEBOOKS_URL = 'http://www.it-ebooks.info/'


def remove_itebooks_wm(output_filename, input_filename):
    with open_pdf(input_filename) as pdf:
        for page in pdf.pages:
            if Name.Annots in page:
                remove_from_page_annotations(page.Annots)
            if Name.Contents in page:
                remove_from_page_contents(page.Contents)
        pdf.save(output_filename)


def remove_from_page_annotations(annotations):
    for i in range(len(annotations)):
        annot = annotations[i]
        if annot.Type != Name.Annot:
            continue
        if annot.Subtype != Name.Link:
            continue
        try:
            if annot.A.Type != Name.Action:
                continue
            if annot.A.S != Name.URI:
                continue
            if annot.A.URI != ITEBOOKS_URL:
                continue
            del annotations[i]
        except AttributeError as ex:
            continue


def remove_from_page_contents(contents):
    for i in range(len(contents)):
        content = contents[i]
        if not Name.LC in content:
            continue
        if content.LC != Name.QQAP:
            continue
        buffer = content.read_bytes()
        if ITEBOOKS_RX.search(buffer):
            del contents[i]


if __name__ == '__main__':
    parser = ArgumentParser(description='remove it-ebooks watermark')
    parser.add_argument('-i', '--input-filename', required=True,
        help='is the name of the input file')
    parser.add_argument('-o', '--output-filename', required=True,
        help='is the name of the output file')
    args = parser.parse_args()
    remove_itebooks_wm(args.output_filename, args.input_filename)

# EOF