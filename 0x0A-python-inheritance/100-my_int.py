#!/usr/bin/python3
"""defines a class Myint that inherits from int"""


class MyInt(int):
    """invert int operators == and !=."""

    def __eq__(self, value):
        """overrides == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """override != operator with == behavior."""
        return self.real == value
