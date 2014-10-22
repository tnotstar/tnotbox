#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from ceODBC import connect

print("Beginning...")

print("Connecting...")
conn = connect(r'dsn=WAPanel')

print("Creating a new cursor object...")
cursor = conn.cursor()

print("Executing a query...")
cursor.execute("SELECT * FROM DAILY_MARKETING_PROGRAMS")
for row in cursor.fetchall():
    print(">", row)

print("Closing the cursor...")
cursor.close()

print("Closing connection...")
conn.close()

print("Finished!")

# EOF