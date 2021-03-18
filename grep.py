#!/usr/bin/env python3

import sys

pattern = sys.argv[1]
path = sys.argv[2]
with open(path) as file:
    for line in file:
        if pattern in line:
            print(line, end="")
