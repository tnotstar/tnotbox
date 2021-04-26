#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pikepdf import Pdf, Name, open as open_pdf
from urllib.parse import urlparse
from argparse import ArgumentParser
from datetime import datetime


BLACK_LISTED_DOMAINS = (
    'www.it-ebooks.info',
    'www.allitebooks.org',
    'www.allitebooks.com',
)


def remove_known_watermarks(arguments):
    with open_pdf(arguments.input_filename) as pdf:
        remove_known_metadata(arguments, pdf.open_metadata())
        for page in pdf.pages:
            if Name.Annots in page:
                remove_watermarks_from_annots(page.Annots)
        if arguments.output_filename:
            pdf.save(arguments.output_filename)


def remove_known_metadata(arguments, metadata):
    print(metadata, metadata['xmpMM:InstanceID'])
    return
    for name in (Name.Creator, Name.Producer, Name.Subject):
        if name in metadata:
            object = metadata.get(name)
            print(str(object), str(object) in BLACK_LISTED_DOMAINS, [ _ for _ in dir(metadata) if not _.startswith('_') ])
            if str(object) in BLACK_LISTED_DOMAINS:
                del object
    if Name.Author in metadata and arguments.author:
        metadata.Author = arguments.author
    if Name.Title in metadata and arguments.title:
        metadata.Title = arguments.title
    if Name.ModDate in metadata:
        metadata.ModDate = datetime.now().strftime('D:%Y%m%d%H%M%S%z')


def remove_watermarks_from_annots(annotations):
    removables = []
    for index, annotation in enumerate(annotations):
        if Name.Annot != annotation.Type:
            continue
        if Name.Link != annotation.Subtype:
            continue
        if not Name.A in annotation:
            continue
        action = annotation.A
        if Name.S not in action:
            continue
        if Name.URI not in action:
            continue
        netloc = parse_uri(action.URI)
        if netloc not in BLACK_LISTED_DOMAINS:
            continue
        removables.append(index)
    for index in removables:
        del annotations[index]


def parse_uri(object):
    uri = urlparse(str(object))
    netloc = uri.netloc or uri.path
    nparts = netloc.split(':')
    if len(nparts) > 0:
        netloc = nparts[0]
    return netloc


if __name__ == '__main__':
    parser = ArgumentParser(description='remove known watermarks in ebooks')
    parser.add_argument('-o', '--output-filename', required=True,
        help='the name of the output file')
    parser.add_argument('-i', '--input-filename', required=True,
        help='the name of the input file')
    parser.add_argument('-A', '--author', help='metadata for author name')
    parser.add_argument('-T', '--title', help='metadata for title')
    arguments = parser.parse_args()
    remove_known_watermarks(arguments)

# EOF