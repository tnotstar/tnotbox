#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

def on_click_me():
    label1 = Label(root, text="Look! I clicked a button!")
    label1.pack()

# this one creates a button
button1 = Button(root, text="Click Me!", pady=2, command=on_click_me, fg="red")
button1.pack()

root.mainloop()

# EOF