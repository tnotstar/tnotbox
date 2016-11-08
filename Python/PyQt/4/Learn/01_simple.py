#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Based upon ZetCode PyQt4 tutorial, at: http://zetcode.com/gui/pyqt4/firstprograms/
"""

from PyQt4 import QtGui

import sys

def main():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle("Simple")
    w.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# EOF