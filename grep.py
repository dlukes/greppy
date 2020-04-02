#!/usr/bin/env python3
# docstring = dokumentační řetězec; uloží se do kouzelné
# proměnné __doc__
"""Usage: grep.py PATTERN FILE

Print lines from FILE matching regular expression PATTERN.

"""
import sys
import regex as re

def grep(pattern, lines, line_numbers):
    """Print lines matching pattern."""
    for index, line in enumerate(lines):
        line = line.strip()
        if re.search(pattern, line):
            if line_numbers:
                print(index + 1, end="|")
            print(line)

def parse_argv(argv):
    args = {
        "line_numbers": False,
        "begin_context": False,
    }
    if "-L" in argv:
        args["line_numbers"] = True
        index = argv.index("-L")
        del argv[index]
    if "-B" in argv:
        args["begin_context"] = True
        index = argv.index("-B")
        del argv[index]
    args["pattern"] = argv[1]
    args["path"] = argv[2]
    return args

def main():
    try:
        args = parse_argv(sys.argv)
    except ValueError:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)

    try:
        with open(args["path"]) as file:
            grep(args["pattern"], file, args["line_numbers"])
    except FileNotFoundError as err:
        print(__doc__.strip(), file=sys.stderr)
        print(err, file=sys.stderr)
        sys.exit(1)

main()