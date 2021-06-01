#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2021, Antonio Alvarado Hernández

from json import load as load_json
from argparse import ArgumentParser

from pikepdf import Pdf as PDF, OutlineItem


def replace_outline(arguments):

    def append_subnodes(outline, nodes):
        for node in nodes:
            if "title" in node and "page" in node:
                print(node["title"], node["page"])
                outline.append(OutlineItem(node["title"], node["page"]))
            if "children" in node:
                append_subnodes(outline, node["children"])

    template = load_json(open(arguments.template_filename, encoding="utf-8"))
    pdf = PDF.open(arguments.input_filename)
    with pdf.open_outline() as outline:
        del outline.root[:]
        append_subnodes(outline.root, template)
    pdf.save(arguments.output_filename)


if __name__ == "__main__":
    description = "a pdf outline replacement utility"
    parser = ArgumentParser(description=description)
    parser.add_argument("-i", "--input-filename", required=True,
        help="the filename of the input pdf file")
    parser.add_argument("-t", "--template-filename", required=True,
        help="the filename of the replacement template")
    parser.add_argument("-o", "--output-filename", required=True,
        help="the filename of the output pdf file")
    args = parser.parse_args()

    replace_outline(args)

# EOF