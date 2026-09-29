#!/usr/bin/python3

from sys import argv

def downcase_it(s: str):
    return s.lower()

if len(argv) == 1:
    print("none")
else:
    print(*(downcase_it(arg) for arg in argv[1:]), sep="\n")

