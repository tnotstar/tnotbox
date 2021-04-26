#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pikepdf import Pdf


TITLE_MAP = {
    'front-matter': 'Front Matter',
    'Introduction': 'Introduction',
    'C01': '1. Individual decision',
    'C02': '2. The elementary market',
    'C03': '3. Game situations',
    'C04': '4. Market with irreversibilities',
    'C05': '5. Mimetic interactions',
    'C06': '6. Competition between firms',
    'C07': '7. Organization of the firm',
    'C08': '8. Emergence of institutions',
    'C09': '9. State and economic system regulation',
    'back-matter': 'Epilogue',
}


def rename_outline_item(output_filename, input_filename, title_map):
    pdf = Pdf.open(input_filename)
    with pdf.open_outline() as outline:
        for item in outline.root:
            if item.title in title_map:
                print(item.title, title_map[item.title])
                item.title = title_map[item.title]
    pdf.save(output_filename)


if __name__ == "__main__":
    rename_outline_item("wow.pdf", "dale.pdf", TITLE_MAP)

# EOF