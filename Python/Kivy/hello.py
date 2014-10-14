#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button


class HelloApp(App):
    def build(self):
        return Button(text='Hello, world!')


if __name__ == '__main__':
    HelloApp().run()

# EOF
