#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import contextlib
import sqlite3 as db


SQL_CREATE_TABLE = r"""
    CREATE TABLE IF NOT EXISTS corpus_rae (
        ordinal,
        word,
        absfreq,
        normfreq
    );
"""

SQL_TRUNCATE_TABLE = r"DELETE FROM corpus_rae;"

SQL_INSERT_VALUES = r"""
    INSERT INTO corpus_rae (ordinal, word, absfreq, normfreq)
    VALUES (?, ?, ?, ?);
"""

def parse_corpus_file(filename):
    corpus = []
    with open(filename, encoding="utf-8") as stream:
        for line in [_.strip() for _ in stream]:
            tokens = line.split("\t")
            if len(tokens) < 4:
                continue

            (ordinal, word, absfreq, normfreq) = tokens

            ordinal = int(ordinal.replace(".", ""))
            word = word.strip()
            absfreq = int(absfreq.replace(",", ""))
            normfreq = float(normfreq.replace(",", ""))

            corpus.append((ordinal, word, absfreq, normfreq))
    return corpus


def create_database(filename, corpus):
    with contextlib.closing(db.connect(filename)) as connect:
        cursor = connect.cursor()
        cursor.execute(SQL_CREATE_TABLE)
        cursor.execute(SQL_TRUNCATE_TABLE)
        for (ordinal, word, absfreq, normfreq) in corpus:
            cursor.execute(SQL_INSERT_VALUES,
                (ordinal, word, absfreq, normfreq))
        connect.commit()


if __name__ == "__main__":
    corpus = parse_corpus_file(r"10000_formas.TXT")
    create_database("corpus.db", corpus)

# EOF