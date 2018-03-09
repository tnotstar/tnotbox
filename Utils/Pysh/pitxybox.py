#!/usr/bin/env python3
#
# Copyright (c) 2018 Antonio Alvarado Hernández - All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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