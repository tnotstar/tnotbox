#!/usr/bin/env python3
# -*- coding:f-8 -*-

import teradata

udaexec = teradata.UdaExec()

with udaexec.connect("tdprod") as session:
    for row in session.execute("SELECT GetQueryBand()"):
        print(row)
    for row in session.execute("SELECT * FROM DBC.DBCInfo"):
        print(row)

# EOF
