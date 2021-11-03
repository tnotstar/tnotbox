# -*- coding: utf-8 -*-

class Portfolio(object):
    """A simple stock portfolio"""
    def __init__(self):
        self.stocks = []

    def buy(self, name, shares, price):
        """Buy `shares` shares of `name` at `price`"""
        self.stocks.append([ name, shares, price ])

    def cost(self):
        """What was the total cost of this portfolio"""
        return sum([ shares*price for name, shares, price in self.stocks ])

# EOF
