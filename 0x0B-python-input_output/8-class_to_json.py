#!/usr/bin/python3
"""defines a python class to JSON function"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structures"""
    return obj.__dict__
