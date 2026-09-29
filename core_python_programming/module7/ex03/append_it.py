#!/usr/bin/python3

from sys import argv

if len(argv) == 1:
    print("none")
else:
    print(*(f"{arg}ism" for arg in argv[1:] if arg.find("ism") == -1), sep="\n")
