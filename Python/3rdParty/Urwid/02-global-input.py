#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urwid as uw

def main():
    text = uw.Text("Hello, World! (Press Q to exit)")
    filler = uw.Filler(text, "top")

    def show_or_exit(key):
        if key in ('q', 'Q', 'esc'):
            raise uw.ExitMainLoop()
        text.set_text(str(key))

    loop = uw.MainLoop(filler, unhandled_input=show_or_exit)  # type: ignore
    loop.run()


if __name__ == '__main__':
    main()

