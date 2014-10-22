#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function

from gi.repository import Gtk


class MainWindow(Gtk.Window):
    
    def __init__(self):
        super(MainWindow, self).__init__(title="My Edit!")
        self.connect("delete-event", self.on_delete_event)
        self.connect("destroy", self.on_destroy)
        self.set_default_size(700, 400)

    def on_file_new(self, widget, data=None):
        pass

    def on_file_open(self, widget, data=None):
        pass

    def on_file_save(self, widget, data=None):
        pass

    def on_file_save_as(self, widget, data=None):
        pass

    def on_file_quit(self, widget, data=None):
        pass

    def on_delete_event(self, widget, data=None):
        print("on_delete_event")
        print(type(data))
        return False

    def on_destroy(self, widget, data=None):
        print("on_destroy")
        print(type(data))
        Gtk.main_quit()


def main():
    win = MainWindow()
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()

# EOF
