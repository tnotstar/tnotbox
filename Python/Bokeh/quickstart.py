#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bokeh.plotting import output_file, figure, show

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

output_file("quickstart.html")

p = figure(title="Simple line example", x_axis_label="x", y_axis_label="y")
p.line(x, y, legend="Temp.", line_width=2)

show(p)

# EOF