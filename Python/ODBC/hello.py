#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import expanduser, abspath

try:
    import ceODBC as odbc
except ModuleNotFoundError:
    import pyodbc as odbc


DSN_FILENAME = r"~/Resources/ODBC/TD_Production_Trusted.dsn"
SQL_VERSION_INFO = r"""
    SELECT I.InfoData
      FROM DBC.DBCInfo AS I
     WHERE I.InfoKey = 'VERSION'
"""


def hello(connect_string):
    try:
        db = odbc.connect(connect_string)
        cursor = db.cursor()
        cursor.execute(SQL_VERSION_INFO)
        for row in cursor:
            print("Connected to the Teradata {} database".format(row[0]))
        cursor.execute("SELECT 'Hello, world!';")
        for row in cursor:
            print("> {}".format(row[0]))
        cursor.close()

    except odbc.DatabaseError as ex:
        print("Oops: {}".format(ex))

    finally:
        db.close()
        print("Connection closed!")


if __name__ == "__main__":
    dsn_fname = abspath(expanduser(DSN_FILENAME))
    connect_string = "FILEDSN={0};".format(dsn_fname)
    hello(connect_string)

# EOF