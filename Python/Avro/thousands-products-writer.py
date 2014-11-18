#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function

from math import log
from time import clock

from avro.io import DatumReader, DatumWriter
from avro.datafile import DataFileReader, DataFileWriter

import avro.schema

def write_fake_products(fname, products_nr=1000):
    digits_nr = int(log(products_nr)/log(10))
    schema = avro.schema.parse(open("Product.avsc").read())
    writer = DataFileWriter(open(fname, "w"), DatumWriter(), schema)
    for i in range(products_nr):
        j = i + 1
        id = str(j).zfill(digits_nr)
        descr = "This is the description #{}".format(j)
        writer.append(dict(id=id, description=descr))
    writer.close()

if __name__ == '__main__':
    start = clock()
    write_fake_products("products-data.avro", 1000000)
    print("Ellapse time {}s".format(clock() - start))

# EOF
