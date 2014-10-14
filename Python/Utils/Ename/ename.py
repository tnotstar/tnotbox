#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk




class EnameMainWindow(ttk.Frame):
    """This is the program's main window.
    """

    def __init__(self, root=None):
        """Initializes given frame instance."""
        super().__init__(master=root, borderwidth=3, relief=SUNKEN)
        root.title("Enamer v{major}.{minor}")
        # Blah, blah, blah, ...
        root.title("Hello, world!")
        # Blah, blah, blah, ...
        self.grid(row=0, column=0)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self._create_widgets()

    def _create_widgets(self):
        """Blah, blah, blah, ..."""
        input_group = ttk.LabelFrame(self, text="Input filename:")
        input_fname = ttk.Entry(input_group)
        input_browse = ttk.Button(input_group, text="...")
        naming_group = ttk.LabelFrame(self, text="Naming options:")
        naming_entry = ttk.Entry(naming_group)
        #
        naming_options = ttk.Frame(naming_group)
        naming_options.grid(row=0, column=1)
        #
        naming_author = ttk.Frame(naming_options)
        ttk.Button(naming_author, text=">").grid(row=0, column=0)
        ttk.Entry(naming_author).grid(row=0, column=1)
        naming_author.grid(row=0, column=0)
        #
        naming_title = ttk.Frame(naming_options)
        ttk.Button(naming_title, text=">").grid(row=0, column=0)
        ttk.Entry(naming_title).grid(row=0, column=1)
        naming_title.grid(row=1, column=0)

        output_group = ttk.LabelFrame(self)
        output_fname = ttk.Entry(self)
        output_browse = ttk.Button(self, text="...")
        rename = ttk.Button(self, text="Rename")
        cancel = ttk.Button(self, text="Cancel")

        input_group.grid(row=0, column=0, sticky=(W, E))
        naming_group.grid(row=1, column=0, sticky=(W, E))
        output_group.grid(row=2, column=0, sticky=(W, E))

        input_fname.grid(row=0, column=1)
        input_browse.grid(row=0, column=2)
        naming_entry.grid(row=0, column=0)


def main():
    """This is the program's entry-point."""
    root = Tk()
    main = EnameMainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()

# EOF
