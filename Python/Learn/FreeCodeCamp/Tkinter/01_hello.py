#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

# this is the main widget
root = Tk()

# this is a single label
label1 = Label(root, text="Hello, world!")
# this organize `label1` onto its parent widget
label1.pack()

# this is the main event loop
root.mainloop()

# EOF