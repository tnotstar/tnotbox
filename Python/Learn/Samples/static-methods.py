#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# sample code from: http://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods

from __future__ import print_function

class Pizza(object):
    def __init__(self, size):
        self._size = size
    def get_size(self):
        return self._size

def test_no_1():
    print("-*- Test #1 -*-")
    print(Pizza.get_size)
    print(Pizza.get_size(Pizza(42)))

def test_no_2():
    print("-*- Test #2 -*-")
    print(Pizza(42).get_size)
    print(Pizza(42).get_size())

def test_no_3():
    print("-*- Test #3 -*-")
    m = Pizza(42).get_size
    print(m)
    print(m())

def test_no_4():
    print("-*- Test #4 -*-")
    m = Pizza(42).get_size
    print(m.__self__)
    print(m.__self__.get_size)
    print(m.__self__.get_size())

class StaticPizza(object):
    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)

def test_no_5():
    print("-*- Test #5 -*-")
    print(StaticPizza().cook is StaticPizza.cook)
    print(StaticPizza().mix_ingredients is StaticPizza.mix_ingredients)
    print(StaticPizza().mix_ingredients is StaticPizza().mix_ingredients)

class ClassPizza(object):
    radius = 42
    @classmethod
    def get_radius(cls):
        return cls.radius

def test_no_6():
    print("-*- Test #6 -*-")
    print(ClassPizza.get_radius)
    print(ClassPizza().get_radius)
    print(ClassPizza.get_radius is ClassPizza().get_radius)
    print(ClassPizza.get_radius())

if __name__ == '__main__':
    # introduction
    test_no_1()
    test_no_2()
    test_no_3()
    test_no_4()
    # static methods!
    test_no_5()
    # class methods!
    test_no_6()
    # to be continue...

# EOF