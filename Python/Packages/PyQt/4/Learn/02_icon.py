#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Based upon ZetCode PyQt4 tutorial, at: http://zetcode.com/gui/pyqt4/firstprograms/
"""

from PyQt4 import QtGui

import sys

class Window(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QtGui.QIcon("web.png"))
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    wnd = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# EOF