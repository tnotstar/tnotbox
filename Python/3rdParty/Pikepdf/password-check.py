#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from pikepdf import Pdf, PasswordError


def password_check(filename):
    for dni in range(51400000, 51500000):
        password = str(dni).rjust(8, "0") + get_dni_control_digit(dni)
        try:
            with Pdf.open(filename, password=password) as pdf:
                print("Gotcha! File {} has {} page(s)!!".
                    format(filename, len(pdf.pages)))
            return
        except PasswordError as ex:
            continue


def get_dni_control_digit(dni):
    return "TRWAGMYFPDXBNJZSQVHLCKE"[int(dni) % 23]


if __name__ == "__main__":
    parser = ArgumentParser(description="a sample of password checking")
    parser.add_argument("-i", "--input-file", required=True,
        help="the name of the input file")
    args = parser.parse_args()

    password_check(args.input_file)

# EOF