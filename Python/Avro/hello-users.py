#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Borrowed from http://avro.apache.org/docs/1.7.6/gettingstartedpython.html
#

from __future__ import absolute_import, unicode_literals, print_function

from avro.io import DatumReader, DatumWriter
from avro.datafile import DataFileReader, DataFileWriter

import avro.schema


schema = avro.schema.parse("""
    {
        "namespace": "examples",
        "type":      "record",
        "name":      "User",
        "fields":    [
          { "name": "name",  "type": "string" },
          { "name": "favorite_number", "type": ["int", "null"] },
          { "name": "favorite_color", "type": ["string", "null"] }
        ]
    }
    """)

writer = DataFileWriter(open("users-data.avro", "w"), DatumWriter(), schema)
writer.append(dict(name="Alyssa", favorite_number=256))
writer.append({"name": "Ben", "favorite_color": "red"})
writer.close()

reader = DataFileReader(open("users-data.avro"), DatumReader())
for user in reader:
    print(user)
reader.close()

# EOF
