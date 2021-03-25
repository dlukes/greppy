#!/usr/bin/env python3

import sys
import re

pattern = sys.argv[1]
path = sys.argv[2]
with open(path) as file:
    for line in file:
        if re.search(pattern, line):
            print(line, end="")
