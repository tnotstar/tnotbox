#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

label1 = Label(root, text="Hello, world!")
label2 = Label(root, text=" ʕ•ᴥ•ʔ ")
label3 = Label(root, text="My name is Antonio")

# following lines uses the grid positioning system
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
label3.grid(row=2, column=2)

root.mainloop()

# EOF