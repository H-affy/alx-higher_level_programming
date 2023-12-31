#!/usr/bin/python3
"""defines a rectangle class"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
        width (int): The width of the new rectangle.
        height (int): the height oof the new rectangle.
        """

        self.height = height
        self.width = width

    @property
    def height(self):
        """setd the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
