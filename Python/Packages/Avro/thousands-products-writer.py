#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function

import os
import os.path
import csv
import math
import time
import sqlite3

from avro.io import DatumReader, DatumWriter
from avro.datafile import DataFileReader, DataFileWriter

import avro.schema

AVRO_SCHEMA = """
{ "namespace": "funnyco",
  "name": "product",
  "type": "record",
  "fields": [
    { "name": "id", "type": "string" },
    { "name": "descript", "type": "string" }
  ]
}
"""

SQLITE3_SCHEMA = """
CREATE TABLE products (
  id,
  descript
)
"""

SQLITE3_INSERT = """
INSERT INTO
  products(id, descript)
VALUES
  (:id, :descript)
"""


def avro_write_fake_products(fname, products_nr):
    schema = avro.schema.parse(AVRO_SCHEMA)
    writer = DataFileWriter(open(fname, "w"), DatumWriter(), schema)
    for p in products_generator(products_nr):
        writer.append(p)
    writer.close()

def csv_write_fake_products(fname, products_nr):
    with open(fname, "w") as stream:
        writer = csv.DictWriter(stream, fieldnames=("id", "descript"))
        for p in products_generator(products_nr):
            writer.writerow(p)

def sqlite3_write_fake_products(fname, products_nr):
    if os.path.exists(fname):
        os.unlink(fname)
    connect = sqlite3.connect(fname)
    connect.execute(SQLITE3_SCHEMA)
    for p in products_generator(products_nr):
        connect.execute(SQLITE3_INSERT, p)
    connect.commit()

def products_generator(products_nr=1):
    for i in range(products_nr):
        id = str(i + 1)
        descript = "This is a description"
        yield dict(id=id, descript=descript)

if __name__ == '__main__':
    PRODUCTS_NR = 1000000
    start = time.clock()
    avro_write_fake_products("products-data.avro", PRODUCTS_NR)
    print("> Avro's elapsed time {}s".format(time.clock() - start))
    start = time.clock()
    csv_write_fake_products("products-data.csv", PRODUCTS_NR)
    print("> CSV's elapsed time {}s".format(time.clock() - start))
    start = time.clock()
    sqlite3_write_fake_products("products-data.db", PRODUCTS_NR)
    print("> SQLite3's elapsed time {}s".format(time.clock() - start))

# EOF
