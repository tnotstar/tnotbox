#!/usr/bin/env python3
#
# Copyright (c) 2018 Antonio Alvarado Hernández - All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from os.path import abspath, expanduser
from mailbox import mbox
from email.header import decode_header, make_header
from email.utils import parseaddr

import re
import sys


LISTSEP_RX = re.compile(r',\s*')
LATIN_XT = str.maketrans("áéíóúñÁÉÍÓÚÑ\n\r\t", "aeiounAEIOUN   ")


def parse_mailbox(fname):
    addresses = dict()
    for message in mbox(fname).itervalues():
        parse_message(addresses, message)
    return addresses

def parse_message(addresses, message):
    for what in ["from", "to"]:
        field = message[what]
        if not field:
            continue
        header = str(make_header(decode_header(field)))
        parse_header(addresses, header)

def parse_header(addresses, header):
    for address in LISTSEP_RX.split(header):
        value, key = parseaddr(address)
        tokens = value.translate(LATIN_XT).split()
        value = " ".join([_.strip().upper() for _ in tokens])
        key = key.lower()
        if not value or not key:
            continue
        if not key in addresses:
            addresses[key] = set()
        addresses[key].add(value)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", help="is the mbox input file name",
        required=True)
    args = parser.parse_args()
    addresses = parse_mailbox(abspath(expanduser(args.input)))
    for address in addresses:
        print(address, ":", sep="")
        for name in sorted(addresses[address]):
            print("> ", name)

# EOF