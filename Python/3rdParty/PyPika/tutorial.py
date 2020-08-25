#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# this code has been based upon:
# https://pypika.readthedocs.io/en/latest/2_tutorial.html
#

from pypika import Table, Query, Field

def sample_1():
    q = Query.from_("customers").select("id", "fname", "lname", "phone")
    print(str(q))
    print(q.get_sql())


def sample_2():
    customers = Table("customers")
    q = Query.from_(customers).select(customers.id, customers.fname,
            customers.lname, customers.phone)
    print(q)

def sample_3():
    Table("x_view_customers").as_("customers")
    q = Query.from_(customers).select(customers.id, customers.phone)
    print(q)

if __name__ == "__main__":
    print("Beginning...")
    sample_1()
    sample_2()
    print("Finished!!")

# EOF