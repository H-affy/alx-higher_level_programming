#!/usr/bin/python3
"""defines a text reading function"""


def read_file(filename=""):
    """Print the contents of a UTF8 test file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
