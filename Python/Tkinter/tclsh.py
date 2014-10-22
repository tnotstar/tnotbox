#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# More info at: https://wiki.python.org/moin/How%20Tkinter%20can%20exploit%20Tcl/Tk%20extensions

import tkinter

def main():
    tclsh = tkinter.Tcl()
    tclsh.eval("""puts {Hello, world!}""")

if __name__ == '__main__':
    main()

# EOF