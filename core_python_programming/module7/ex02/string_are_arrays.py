#!/usr/bin/python3

from sys import argv

if len(argv) != 2 or argv[1].count("z") == 0:
    print("none")
else:
    # print(argv[1].count("z") * "z")
    for c in argv[1]:
        if c == "z":
            print("z", end="")

    print()
