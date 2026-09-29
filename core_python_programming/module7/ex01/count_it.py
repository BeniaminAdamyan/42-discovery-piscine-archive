#!/usr/bin/python3

from sys import argv

if len(argv) == 1:
    print("none")
else:
    print("parameters:", len(argv) - 1)
    print(*(f"{arg}: {len(arg)}" for arg in argv[1:]), sep="\n")
