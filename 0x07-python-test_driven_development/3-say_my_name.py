#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    The function print My name is <first name> <last name>

    Args:
    fist_name: the first name to print.
    last_name: The last name to print

    Raise:
    TypeError: if either of first_name or last_name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
