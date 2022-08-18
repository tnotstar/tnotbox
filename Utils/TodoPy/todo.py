# Copyright 2021-2022, Antonio Alvarado Hernández
# -*- coding: utf-8 -*-

from argparse import ArgumentParser


def main():
	synopsis = "todo.py - a command line TODO list in Python3"
	parser = ArgumentParser(description=synopsis)
	subparsers = parser.add_subparsers()
	init = subparsers.add_parser("init")
	add = subparsers.add_parser("add")
	add.add_argument("item", type=str, help="an item to be added to the list")
	ls = subparsers.add_parser("ls")
	rm = subparsers.add_parser("rm")
	check = subparsers.add_parser("check")
	destroy = subparsers.add_parser("destroy")

	args = parser.parse_args()
	print(args)


if __name__ == "__main__":
	main()

# EOF
