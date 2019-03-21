#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

frame1 = Frame(root, border=4, relief=RIDGE)
frame1.grid(sticky=W)
frame2 = Frame(root, border=4, relief=RIDGE)
frame2.grid(sticky=W)
frame1.columnconfigure(0, weight=1)
frame2.columnconfigure(0, weight=1)

label1 = Label(frame1, text='short', background='white')
label1.grid(sticky=(W, E))
label2 = Label(frame2, text='quite a bit longer', background='white')
label2.grid(sticky=(W, E))

root.mainloop()

# EOF