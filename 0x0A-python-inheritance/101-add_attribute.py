#!/usr/bin/python3
"""defines a function that add attributes to objects"""

def add_attribute(obj, attr, value):
    """add a new attribute to an object if possible.

    Args:
    obj (any): The object to add an attribute
    attr (str): The name of the attributes to add to object
    value (any): The value of attribute

    Raises:
    TypeError: if the attribute cannot be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
