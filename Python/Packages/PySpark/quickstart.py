#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Start with:
#
#   $ bin/spark-submit <your-path>/quickstart.py
#

from pyspark import SparkContext

log = "README.md"
sc = SparkContext("local", "Basic Example")
data = sc.textFile(log).cache()

numAs = data.filter(lambda s: "a" in s).count()
numBs = data.filter(lambda s: "b" in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

# EOF
