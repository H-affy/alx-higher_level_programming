#!/usr/bin/python3
"""define the rectangle class"""


class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
        width (int): The width of the new rectangle
        height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set/get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """return a printable representation of the rectangle
        represent the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
