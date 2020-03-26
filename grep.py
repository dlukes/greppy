#!/usr/bin/env python3

import sys

pattern, path = sys.argv[1:]
with open(path) as file:
    for line in file:
        if pattern in line:
            print(line, end="")