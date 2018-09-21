#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes

MB_OK = 0x0
ICON_INFO = 0x40
MessageBox = ctypes.windll.user32.MessageBoxW


if __name__ == "__main__":
    MessageBox(0, "Hello, Windows!", "Information", MB_OK | ICON_INFO)

# EOF