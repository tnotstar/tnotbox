#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

import cx_Oracle


def hello(connect_string):
    try:
        db = cx_Oracle.connect(connect_string)
        print("Connected to the Oracle {} database".format(db.version))
        cursor = db.cursor()
        cursor.execute("SELECT 'Hello, world!' FROM dual")
        for row in cursor:
            print("> {}".format(row[0]))

    except cx_Oracle.DatabaseError as ex:
        print("Oops: {}".format(ex))

    finally:
        db.close()
        print("Connection closed!")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("connect_string")
    args = parser.parse_args()
    hello(args.connect_string)

# EOF