#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function

from gi.repository import Gtk


class MyWindow(Gtk.Window):
    
    def __init__(self):
        super(MyWindow, self).__init__(title="Hello, world!")
        self.click_me = Gtk.Button(label="Click Me!")
        self.click_me.connect("clicked", self.on_button_clicked)
        self.add(self.click_me)
        self.connect("delete-event", Gtk.main_quit)

    def on_button_clicked(self, widget):
        print("Hello, world!")


def main():
    win = MyWindow()
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()

# EOF
