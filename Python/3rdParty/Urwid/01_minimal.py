#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urwid as uw

def main():
    text = uw.Text("Hello, World!")
    filler = uw.Filler(text, "top")
    loop = uw.MainLoop(filler)
    loop.run()


if __name__ == '__main__':
    main()

