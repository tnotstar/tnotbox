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

import os
import sys
import inspect

import pprint as pp


class Shell(object):
    """Blah, blah, blah, ..."""

    def __init__(self, stdin=None, stdout=None):
        """Initialize given shell instance."""
        self._stdin = stdin or sys.stdin
        self._stdout = stdout or sys.stdout
        self._builtins = self._make_builtins()

    def run(self):
        print("> Beginning...")
        print(">", ", ".join(sorted(self._builtins.keys())))
        print("----------------")
        self._builtins["pwd"]()()
        print("----------------")
        print("> Finished!")

    def _make_builtins(self, which=__name__):
        """Make a list with internal commands."""
        def iscommand(what):
            if not inspect.isclass(what):
                return False
            return issubclass(what, Command) and what != Command
        return dict([
            (cls.cmdname(), cls) for _, cls in
                    inspect.getmembers(sys.modules[which], iscommand)
        ])

class Command(object):
    """A base class to implement commands."""

    @classmethod
    def cmdname(cls):
        name = str.lower(cls.__name__)
        if name.endswith("cmd"):
            return name[:-3]
        return name

    def __init__(self):
        self._out = sys.stdout
        self._err = sys.stderr
        self._in = sys.stdin

    def __call__(self):
        self._out.write("Called from {}\n".format(self.__class__.__name__))

class CommandCmd(Command):
    """Blah, blah, blah, ..."""

class AliasCmd(Command):
    """Blah, blah, blah, ..."""

class UnaliasCmd(Command):
    """Blah, blah, blah, ..."""

class RmaliasCmd(Command):
    """Blah, blah, blah, ..."""

class BgCmd(Command):
    """Blah, blah, blah, ..."""

class BreakCmd(Command):
    """Blah, blah, blah, ..."""

class CdCmd(Command):
    """Blah, blah, blah, ..."""
	# aka "chdir"

class PwdCmd(Command):
    def __call__(self):
        self._out.write("{}\n".format(os.getcwd()))

class DotCmd(Command):
    """Blah, blah, blah, ..."""

class EchoCmd(Command):
    """Blah, blah, blah, ..."""

class ExecCmd(Command):
    """Blah, blah, blah, ..."""

class ExpCmd(Command):
    """Blah, blah, blah, ..."""

class ExportCmd(Command):
    """Blah, blah, blah, ..."""

class EvalCmd(Command):
    """Blah, blah, blah, ..."""

class LetCmd(Command):
    """Blah, blah, blah, ..."""

class FalseCmd(Command):
    """Blah, blah, blah, ..."""

class FcCmd(Command):
    """Blah, blah, blah, ..."""

class FgCmd(Command):
    """Blah, blah, blah, ..."""

class GetoptsCmd(Command):
    """Blah, blah, blah, ..."""

class HashCmd(Command):
    """Blah, blah, blah, ..."""

class JobidCmd(Command):
    """Blah, blah, blah, ..."""

class JobsCmd(Command):
    """Blah, blah, blah, ..."""

class LocalCmd(Command):
    """Blah, blah, blah, ..."""

class ReadCmd(Command):
    """Blah, blah, blah, ..."""

class ReturnCmd(Command):
    """Blah, blah, blah, ..."""

class SetCmd(Command):
    """Blah, blah, blah, ..."""

class SetvarCmd(Command):
    """Blah, blah, blah, ..."""

class ShiftCmd(Command):
    """Blah, blah, blah, ..."""

class TimesCmd(Command):
    """Blah, blah, blah, ..."""

class TrapCmd(Command):
    """Blah, blah, blah, ..."""

class TrueCmd(Command):
    """Blah, blah, blah, ..."""

class TypeCmd(Command):
    """Blah, blah, blah, ..."""

class UmaskCmd(Command):
    """Blah, blah, blah, ..."""

class WaitCmd(Command):
    """Blah, blah, blah, ..."""

class UlimitCmd(Command):
    """Blah, blah, blah, ..."""

class UnsetCmd(Command):
    """Blah, blah, blah, ..."""

class WordexpCmd(Command):
    """Blah, blah, blah, ..."""

class LsCmd(Command):
    """Blah, blah, blah, ..."""

class CpCmd(Command):
    """Blah, blah, blah, ..."""

class MvCmd(Command):
    """Blah, blah, blah, ..."""

class RmCmd(Command):
    """Blah, blah, blah, ..."""


if __name__ == '__main__':
    try:
        sh = Shell()
        sh.run()
    except Exception as exc:
        print(str(exc))

# EOF