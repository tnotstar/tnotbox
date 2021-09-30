# single-line comments start with a #

#[
    This is multiline comment.
    In Nim, multiline comments can be nested,
    beginning with #[ and ending with ]#
]#

discard """
This can also work as a multiline comment.
Or for unparsable, broken code.
"""

var
    letter: char = 'n'
    lang = "N" & "im"
    nLength: int = len(lang)
    truth: bool = false

let
    legs = 400
    arms = 2_000
    aboutPi = 3.15

const
    debug = true
    compileBadCode = false

when compileBadCode:
    legs = legs + 1
    const input = readline(stdin)

discard 1 > 2
