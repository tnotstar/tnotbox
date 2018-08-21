#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk


def draw(widget, context, color=(0, 0, 0)):
    context.set_source_rgb(*color)
    context.rectangle(0, 0, widget.get_allocated_width(), widget.get_allocated_height())
    context.fill()


def main():
    window = Gtk.Window()
    window.set_name("MyRuler")
    window.connect("destroy", Gtk.main_quit)

    drawing = Gtk.DrawingArea()
    window.add(drawing)

    drawing.set_size_request(800, 70)
    drawing.connect("draw", draw)
    drawing.show()

    window.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()

# EOF
