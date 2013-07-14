#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def subtract_borrowing(a, b):

    c = n = 0
    while a > 0:
        # extract the rightmost digits
        da = a % 10
        db = b % 10

        # calculate the left tails
        a //= 10
        b //= 10

        # check if we need to borrow
        if da < db:
            a -= 1
            da += 10

        # update the output value
        c += (da - db) * 10**n
        n += 1

    return c

if __name__ == '__main__':
    print(subtract_borrowing(30752,   863))
    print(subtract_borrowing(30752,     0))
    print(subtract_borrowing(30752, 30752))

# EOF
