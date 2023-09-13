#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urwid as uw

PALETTE = [
    ("banner", "black", "yellow"),
    ("streak", "black", "dark red"),
    ("bg",     "black", "dark blue"),
]

def main():
    text = uw.Text(("banner", "Hello, World! (Press Q to exit)"), align="center")
    filler = uw.Filler(uw.AttrMap(text, "streak"))
    mapper = uw.AttrMap(filler, "bg")

    def show_or_exit(key):
        if key in ('q', 'Q', 'esc'):
            raise uw.ExitMainLoop()
        text.set_text(str(key))

    loop = uw.MainLoop(mapper, palette=PALETTE, unhandled_input=show_or_exit)  # type: ignore
    loop.run()


if __name__ == '__main__':
    main()

