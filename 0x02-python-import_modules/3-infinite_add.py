#!/usr/bin/python3
from sys import argv
result = 0
if len(argv) > 1:
    for a in range(1, len(argv)):
        result += int(argv[a])
print(result)
