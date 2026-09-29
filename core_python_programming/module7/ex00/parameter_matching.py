#!/usr/bin/python3

from sys import argv

if len(argv) == 1:
    print("none")
else:
    word = input("What was the parameter? ")

    if word == argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
