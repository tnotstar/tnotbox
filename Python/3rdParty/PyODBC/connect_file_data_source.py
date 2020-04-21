#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import expanduser, abspath

import pyodbc as odbc

DSN_FILENAME = r"~/Resources/ODBC/TD_Trusted_Production.dsn"

def main():
    dsn_fname = abspath(expanduser(DSN_FILENAME))
    print("Using file dsn: {}...".format(dsn_fname))
    print("Connecting to:\n{}\n...".format(open(dsn_fname).read()))
    connect_string = "FILEDSN={0};".format(dsn_fname)
    print("Using connection string: {}...".format(connect_string))
    try:
        cnxn = odbc.connect(connect_string)
    except Exception as exc:
        print("Oops something is wrong: {}".format(exc))
    else:
        print("Connect successfully!")
        cnxn.close()

if __name__ == "__main__":
    main()

# EOF