#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    "Print a string in uppercase."
    for c in str:
        if ord("a")<= ord(c) <= ord("z"):
            c = chr(ord(c) - 32)
        print("{:s}".format(c), end="")
        print()
