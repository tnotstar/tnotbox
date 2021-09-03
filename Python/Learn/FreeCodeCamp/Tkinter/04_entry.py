#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

entry1 = Entry(root, fg="gray", width=50)
entry1.insert(0, "Enter your name here")
entry1.pack()

def on_click_me():
    message = "Hello, {}!".format(entry1.get())
    label1 = Label(root, text=message).pack()

# this one creates a button
button1 = Button(root, text="Say Hello!", pady=2, command=on_click_me)
button1.pack()

root.mainloop()

# EOF