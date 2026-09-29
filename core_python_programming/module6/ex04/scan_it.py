#!/usr/bin/python3

from sys import argv
import re

if len(argv) == 3 and argv[1] in argv[2]:
    print(len(re.findall(fr"\b{argv[1]}\b", argv[2], re.IGNORECASE)))
else:
    print("none")
