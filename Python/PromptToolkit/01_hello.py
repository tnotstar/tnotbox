#!/usr/bin/env python
# -*- coding: utf-8 -*-

from prompt_toolkit import prompt


if __name__ == '__main__':
    answer = prompt("Just say hello: ")
    print("You said: '{0}'!".format(answer))

# EOF
