#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmd


class HelloShell(cmd.Cmd):
    """This is my hello command line minishell implementation."""

    def do_hello(self, arg):
        """Print a hello-world message on the console."""
        if arg:
            print("Hello, {}!".format(arg))
        else:
            print("Hello, world!")
    
    def do_exit(self, args):
        """Exit the print-eval-loop."""
        print("Goodbye, cruel world...")
        return True
    
    do_EOF = do_exit


if __name__ == "__main__":
    HelloShell().cmdloop()

# EOF