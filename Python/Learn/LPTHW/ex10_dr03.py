print("""\
\\\\         Backslash (\\)
\\'          Single-quote (\')
\\"          Double-quote (\")
\\a          ASCII bell (BEL)
\\b          ASCII backspace (BS)
\\f          ASCII formfeed (FF)
\\n          ASCII linefeed (LF)
\\N{name}    Unicode character named "name" (e.g. \\N{colon}==\N{colon})
\\r          ASCII carriage return (CR)
\\t          ASCII horizontal tab (TAB)
\\uxxxx      Unicode character with 16-bit hex value "xxxx"
\\Uxxxxxxxx  Unicode character with 32-bit hex value "xxxxxxxx"
\\v          ASCII vertical tab (VT)
\\000        ASCII character with octal value "000"
\\xhh        ASCII character with hex value "hh"
""")