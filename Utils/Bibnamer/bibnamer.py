#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

import wx


NAME = "Bibname"
VERSION = "0.1.0"
SINOPSIS = "My Biblio files renamer utility"


class Model(object):
    """This is the application model in out mvc implementation."""


class View(wx.Dialog):
    """This is the application view in out mvc implementation."""

    def __init__(self, app):
        super(View, self).__init__()
        self._app = app


class Controller(wx.App):
    """This is the application controller in out mvc implementation."""

    def __init__(self):
        super(App, self).__init__(False)

    def run(self):
        # parse the command line arguments
        args = self._parse_arguments()

        # create the program view and show it
        view = View(self)
        view.Layout()
        view.Show()

        # execute the main loop
        print("Before mainloop...")
        self.MainLoop()
        print("After mainloop!")

    def _parse_arguments(self):
        parser = ArgumentParser(prog=NAME, description=SINOPSIS)
        return parser.parse_args()


if __name__ == "__main__":
    app = App()
    app.run()

# EOF