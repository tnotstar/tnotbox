#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def run_test(do_raise):
    try:
        print("beginning the `try` block...")
        if do_raise:
            print("raising an invalid value exception")
            raise ValueError

    except IOError:
        print("if the exception raised on i/o errors")

    except:
        print("wherever other exception goes here")

    else:
        print("if no exception has raised")

    finally:
        print("...and always say: finished!")

if __name__ == '__main__':
    run_test(True)
    run_test(False)

# EOF
