#!/usr/bin/python3
"""The script define function for inteer addition"""


def add_integer(a, b=98):
    """The function returns the integer addition of a and b"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
