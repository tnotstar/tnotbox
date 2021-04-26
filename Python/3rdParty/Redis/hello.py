#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from redis import Redis

def main():
    r = Redis()
    rs = r.hset("test", mapping={ 'name': 'Joe Doe', 'age': 46 })
    print("> rs = {}".format(rs))
    rs = r.hgetall("test")

if __name__ == "__main__":
    main()

# EOF