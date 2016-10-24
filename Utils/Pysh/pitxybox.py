#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


class BaseCommand(object):
    """Blah, blah, blah, ..."""


class ListCommand(BaseCommand):
    """Blah, blah, blah, ..."""


class CopyCommand(BaseCommand):
    """Blah, blah, blah, ..."""


class MoveCommand(BaseCommand):
    """Blah, blah, blah, ..."""


class RemoveCommand(BaseCommand):
    """Blah, blah, blah, ..."""


class BaseLoop(object):
    """Blah, blah, blah, ..."""

    def __init__(self, stdin=None, stdout=None):
        """Initialize given loop instance."""
        if stdin is not None:
            self.stdin = stdin
        else:
            self.stdin = sys.stdin

        if stdout is not None:
            self.stdout = stdout
        else:
            self.stdout = sys.stdout

        self.commands = dict()
        self.register_all()

    def run(self):
        """Blah, blah, blah, ..."""
        print(">", "Hello, world!")
        for key in self.commands:
            print(">>", key)

    def register(self, name, clazz):
        """Register a command with given name and class."""
        self.commands[name] = clazz

    def register_all(self):
        """Register each command supported by the loop."""


class PitxyLoop(BaseLoop):
    """Blah, blah, blah, ..."""

    def register_all(self):
        """Register each command supported by the loop."""
        self.register("ls", ListCommand)
        self.register("cp", CopyCommand)
        self.register("mv", MoveCommand)
        self.register("rm", RemoveCommand)


if __name__ == '__main__':
    print("Beginning...")
    loop = PitxyLoop()
    loop.run()
    print("Finished!")

# EOF
