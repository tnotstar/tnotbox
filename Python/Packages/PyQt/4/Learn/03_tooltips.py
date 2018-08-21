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
        QtGui.QToolTip.setFont(QtGui.QFont("SansSerif", 10))

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QtGui.QIcon("web.png"))
        self.setToolTip("This is a <b>QWidget</b> widget")

        btn = QtGui.QPushButton("Button", self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    wnd = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# EOF