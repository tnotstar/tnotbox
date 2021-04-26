#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pikepdf import Pdf


TITLE_MAP = {
    'Front Matter': 'Hello, world!'
}


def rename_outline_item(output_filename, input_filename, title_map):
    pdf = Pdf.open(input_filename)
    with pdf.open_outline() as outline:
        for item in outline.root:
            if item.title in title_map:
                item.title = title_map[item.title]
    pdf.save(output_filename)


if __name__ == "__main__":
    rename_outline_item("wow.pdf", "dale.pdf", TITLE_MAP)

# EOF