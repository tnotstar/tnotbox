#!/usr/bin/env python3
# -*- coding: utf-8 -*_

import tomllib as toml
import pprint as pp


TOMLSTR = r"""
# This is a TOML document.

[databases]

[databases.employees]
url = "jdbc:postgresql://localhost:5432"
user = "blake"

[tasks]

[tasks.fetch-employees]
type = "fetch"
description = "Dump employees database"

[tasks.fetch-employees.source]
database = "employees"
query = '''
SELECT *
  FROM employees
 WHERE hire_date > '2000-01-01'
'''

[tests]
integers = [ 1, 2, 3 ]
colors = [ "red", "yellow", "green" ]
nested_arrays_of_ints = [ [ 1, 2 ], [3, 4, 5] ]
nested_mixed_array = [ [ 1, 2 ], ["a", "b", "c"] ]
string_array = [ "all", 'strings', '''are the same''', '''type''' ]

# Mixed-type arrays are allowed
numbers = [ 0.1, 0.2, 0.5, 1, 2, 5 ]
contributors = [
  "Foo Bar <foo@example.com>",
  { name = "Baz Qux", email = "bazqux@example.com", url = "https://example.com/bazqux" }
]
"""

config = toml.loads(TOMLSTR)
pp.pprint(config)

# EOF
