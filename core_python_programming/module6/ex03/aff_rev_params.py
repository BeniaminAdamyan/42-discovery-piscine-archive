#!/usr/bin/python3

from sys import argv

if len(argv) < 3:
    print("none")
else:
    print(*argv[-1:0:-1], sep="\n")
