#!/usr/bin/env python3

"""Usage: grep.py PATTERN FILE

Print lines from FILE matching regular expression PATTERN.

"""

import sys
import re

def grep(pattern, lines):
    """Print lines matching pattern."""
    for line in lines:
        if re.search(pattern, line):
            print(line, end="")

def parse_argv(argv):
    """Parse script arguments."""
    if len(argv) == 3:
        pattern = argv[1]
        path = argv[2]
    else:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)
    return pattern, path

def main():
    """Main entry point of script."""
    pattern, path = parse_argv(sys.argv)
    try:
        with open(path) as file:
            grep(pattern, file)
    except FileNotFoundError as err:
        print(__doc__.strip(), file=sys.stderr)
        print(err, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()