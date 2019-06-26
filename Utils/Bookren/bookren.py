#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

import wx


NAME = "Bookren"
VERSION = "0.0.1"
SINOPSIS = "My Biblio files renamer utility"


class Model(object):
    """This is the application model of our MVC implementation."""


class View(wx.Dialog):
    """This is the application view of our MVC implementation."""

    def __init__(self, app):
        super(View, self).__init__(parent=None, size=(640, 480))
        self.SetTitle(u"{0} - Version {1}".format(NAME, VERSION))
        self._app = app

    def Build(self):
        self.Bind(wx.EVT_CLOSE, self.DoExit)
        self.Layout()
        self.Center()

    def DoExit(self, event):
        self.Destroy()


class Controller(wx.App):
    """This is the application controller of our MVC implementation."""

    def __init__(self):
        super(Controller, self).__init__(False)

    def run(self):
        # parse the command line arguments
        args = self._parse_arguments()

        # create the program view and show it
        view = View(self)
        view.Build()
        view.Show()

        # execute the main loop
        print("Before mainloop...")
        self.MainLoop()
        print("After mainloop!")

    def _parse_arguments(self):
        parser = ArgumentParser(prog=NAME, description=SINOPSIS)
        return parser.parse_args()


if __name__ == "__main__":
    ctrlr = Controller()
    ctrlr.run()

# EOF