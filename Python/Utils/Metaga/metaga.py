#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import csv
import json
import pprint


def parse_json_stream(input_stream):
    raw = json.load(input_stream)
    names = raw.get("attributeNames", [])
    items = raw.get("items", [])
    sheet = []
    sheet.append(["id", "kind"] + names)
    for item in items:
        id = item.get("id")
        kind = item.get("kind")
        attribs = item.get("attributes", {})
        row = [id, kind]
        for name in names:
            if name in attribs:
                cell = attribs.get(name)
            else:
                cell = None
            row.append(cell)
        sheet.append(row)
    return sheet

def write_csv_sheet(output_stream, sheet):
    writer = csv.writer(output_stream)
    for row in sheet:
        writer.writerow(row)

with open("data.json", "r") as input:
    sheet = parse_json_stream(input)

with open("metadata.csv", "w") as output:
    write_csv_sheet(output, sheet)

# EOF
