#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import inspect

import pprint as pp


class Shell(object):
    """Blah, blah, blah, ..."""

    def __init__(self, stdin=None, stdout=None):
        """Initialize given shell instance."""
        if stdin is not None:
            self.stdin = stdin
        else:
            self.stdin = sys.stdin

        if stdout is not None:
            self.stdout = stdout
        else:
            self.stdout = sys.stdout

        self._builtins = self._make_builtins()

    def run(self):
        print("> Beginning...")
        print(">", ", ".join(sorted(self._builtins.keys())))
        print("----------------")
        self._builtins["pwd"]()()
        print("----------------")
        print("> Finished!")

    def _make_builtins(self, which=None):
        """Make a list with internal commands."""

        def iscommand(what):
            if not inspect.isclass(what):
                return False
            return issubclass(what, Command) and what != Command

        return dict(
            [(cls.cmdname(), cls) for _, cls in
                inspect.getmembers(
                        sys.modules[which or __name__],
                        iscommand
                )
            ]
        )

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
