#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import inspect


class Shell(object):
    """Blah, blah, blah, ..."""

    def __init__(self):
        self._builtins = self._make_builtins()

    def run(self):
        print("> Beginning...")
        print(">", ", ".join(sorted(self._builtins.keys())))
        print("----------------")
        self._builtins["pwd"]()()
        print("----------------")
        print("> Finished!")

    def _make_builtins(self, which=None):

        def iscommand(what):
            if not inspect.isclass(what):
                return False
            return issubclass(what, Command) and what != Command

        if not which:
            which = __name__
        module = sys.modules[which]

        builtins = {}
        for _, cls in inspect.getmembers(module, iscommand):
            cmd = cls.cmdname()
            builtins[cmd] = cls
        return builtins

class Command(object):
    """Blah, blah, blah, ..."""

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
    pass

class AliasCmd(Command):
    pass

class UnaliasCmd(Command):
    pass

class RmaliasCmd(Command):
    pass

class BgCmd(Command):
    pass

class BreakCmd(Command):
    pass

class CdCmd(Command):
    pass  # aka "chdir"

class PwdCmd(Command):
    def __call__(self):
        self._out.write("{}\n".format(os.getcwd()))

class DotCmd(Command):
    pass

class EchoCmd(Command):
    pass

class ExecCmd(Command):
    pass

class ExpCmd(Command):
    pass

class ExportCmd(Command):
    pass

class EvalCmd(Command):
    pass

class LetCmd(Command):
    pass

class FalseCmd(Command):
    pass

class FcCmd(Command):
    pass

class FgCmd(Command):
    pass

class GetoptsCmd(Command):
    pass

class HashCmd(Command):
    pass

class JobidCmd(Command):
    pass

class JobsCmd(Command):
    pass

class LocalCmd(Command):
    pass

class ReadCmd(Command):
    pass

class ReturnCmd(Command):
    pass

class SetCmd(Command):
    pass

class SetvarCmd(Command):
    pass

class ShiftCmd(Command):
    pass

class TimesCmd(Command):
    pass

class TrapCmd(Command):
    pass

class TrueCmd(Command):
    pass

class TypeCmd(Command):
    pass

class UmaskCmd(Command):
    pass

class WaitCmd(Command):
    pass

class UlimitCmd(Command):
    pass

class UnsetCmd(Command):
    pass

class WordexpCmd(Command):
    pass


if __name__ == '__main__':
    sh = Shell()
    sh.run()

# EOF
