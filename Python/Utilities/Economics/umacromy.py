#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import numpy as np


class BaseModel(object):
    """TODO"""

    def __init__(self, nplots=1):
        print("Hello, from Base!")
        self._nplots = nplots

    @property
    def nplots(self):
        return self._nplots

class ISMPModel(BaseModel):
    """TODO"""

    def __init__(self):
        super(ISMPModel, self).__init__(nplots=2)
        print("Hello, from ISMP!")

def main():
    """This is the main entry-point while running stand-alone."""
    print("Hello, world!")
    model = ISMPModel()
    print("Model has", model.nplots, "plots")


if __name__ == '__main__':
    main()

# EOF