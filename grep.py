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
    positional = []
    # pomocí funkce iter si vytvoříme iterátor, tj. objekt,
    # ze kterého můžeme postupně tahat prvky nějaké kolekce
    # *na různých místech v kódu*, protože si pamatuje,
    # který prvek nám vydal naposledy a který je na řadě
    # příště
    argv_iter = iter(argv[1:])
    # ve většině případů vytáhneme další prvek z iterátoru
    # argumentů v hlavičce for cyklu...
    for arg in argv_iter:
        if arg == "-L":
            args["line_numbers"] = True
        elif arg == "-B":
            # ... kromě případu, kdy narazíme na argument
            # "-B", pak další prvek vytáhneme rovnou ještě
            # v rámci toho stejného cyklu pomocí funkce next,
            # a použijeme ho jako hodnotu pro přepínač "-B"
            args["begin_context"] = next(argv_iter)
        else:
            positional.append(arg)
    args["pattern"], args["path"] = positional
    return args

def main():
    try:
        args = parse_argv(sys.argv)
    # funkce next může teoreticky vyvolat chybu StopIteration,
    # v případě, že za přepínačem "-B" uživatel nezadal
    # žádnou hodnotu; to je chybné zadání, které chceme
    # odchytit
    except (ValueError, StopIteration):
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