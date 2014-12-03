#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

import re
import sys
import glob
import os.path

RX_FILENAME_TAGS = re.compile(r"^([0-9]+)\.\s+(.+)\,\s+([^,]+)\.[^.]+$")

def tags_from_filename(filename):
    basename = os.path.basename(filename)
    match = RX_FILENAME_TAGS.match(basename)
    if not match:
        return None
    return match.groups()

for pattern in sys.argv[1:]:
    for entry in glob.glob(pattern):
        filename = os.path.abspath(entry)
        if not os.path.isfile(filename):
            continue

        filename_tags = tags_from_filename(filename)
        if not filename_tags:
            continue

        (trackno, title, composer) = filename_tags
        if not trackno or not title or not composer:
            continue

        print(">", filename, ":", trackno, ",", title, ",", composer)
        id3tags = EasyID3()
        id3tags["artist"] = u"Baby Einstein"
        id3tags["album"] = u"Compendium For Ainhoa"
        id3tags["genre"] = u"Classical"
        id3tags["discnumber"] = unicode(1)
        id3tags["tracknumber"] = unicode(int(trackno))
        id3tags["title"] = title
        id3tags["composer"] = composer
        id3tags["performer"] = u"Baby Einstein Music Box Orchestra"
        id3tags.save(filename)

# EOF
