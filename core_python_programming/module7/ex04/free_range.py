#!/usr/bin/python3

from sys import argv

if len(argv) != 3 or not argv[1][0] in ["+", "-"] and not argv[1].isdigit() and argv[2][0] in ["+", "-"] and not argv[2].isdigit() or argv[1] >= argv[2]:
    print("none")
else:
    print([*range(int(argv[1]), int(argv[2]) + 1)])
