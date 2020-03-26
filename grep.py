#!/usr/bin/env python3
# docstring = dokumentační řetězec; uloží se do kouzelné
# proměnné __doc__
"""Usage: grep.py PATTERN FILE

Print lines from FILE matching regular expression PATTERN.

"""
import sys
import regex as re

try:
    pattern, path = sys.argv[1:]
except ValueError:
    print(__doc__.strip(), file=sys.stderr)
    sys.exit(1)

try:
    with open(path) as file:
        for line in file:
            line = line.strip("\n")
            if re.search(pattern, line):
                print(line)
except FileNotFoundError as err:
    print(__doc__.strip(), file=sys.stderr)
    print(err, file=sys.stderr)
    sys.exit(1)