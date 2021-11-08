# -*- coding: utf-8 -*-

from portfolio import Portfolio

import unittest


class PortfolioTest(unittest.TestCase):
    def test_empty_portfolio(self):
        p = Portfolio()
        assert p.cost() == 0

    def test_buy_one_stock(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        assert p.cost() == 17648.0

    def test_buy_two_stocks(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        p.buy("HPQ", 100,  36.15)
        assert p.cost() == 21263.0

# EOF
