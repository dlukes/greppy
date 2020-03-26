#!/usr/bin/env python3

import sys
import regex as re

pattern, path = sys.argv[1:]
with open(path) as file:
    for line in file:
        line = line.strip("\n")
        if re.search(pattern, line):
            print(line)