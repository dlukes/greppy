#!/usr/bin/env python3
# docstring = dokumentační řetězec; uloží se do kouzelné
# proměnné __doc__
"""Print lines from FILE matching regular expression PATTERN.

"""
import sys
import argparse
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
    parser = argparse.ArgumentParser(description=__doc__.strip())
    parser.add_argument("pattern", help="Pattern to match")
    parser.add_argument("path", help="File to search")
    parser.add_argument("-L", "--line-numbers", help="Print line numbers", action="store_true")
    parser.add_argument("-B", "--begin-context", help="Print context", type=int)
    return parser.parse_args(argv[1:])

def main():
    args = parse_argv(sys.argv)

    try:
        with open(args.path) as file:
            grep(args.pattern, file, args.line_numbers)
    except FileNotFoundError as err:
        print(__doc__.strip(), file=sys.stderr)
        print(err, file=sys.stderr)
        sys.exit(1)

main()
