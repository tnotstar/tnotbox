#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import tree


def test1():
    """\
    Stolen from: http://scikit-learn.org/stable/modules/tree.html
    """

    X = [[0, 0], [1, 1]]
    Y = [0, 1]
    dt1 = tree.DecisionTreeClassifier()
    dt1 = dt1.fit(X, Y)

    print(dt1.predict([[2., 2.]]))
    print(dt1.predict([[0., 0.]]))
    print(dt1.predict([[.9, .9]]))


if __name__ == '__main__':
    test1()

# EOF