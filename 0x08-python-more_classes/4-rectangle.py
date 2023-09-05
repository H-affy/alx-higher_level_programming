#!/usr/bin/python3
"""defines a rectangle class"""


class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
        width (int): The width of the new rectangle
        height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of the rectangle"""
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
        """Set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__ width * self.__height)

    def perimeter(self):
        """return The perimeter of the rectangle"""
        if size.__width == 0 or size.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """return a printable representation of the rectangle
        represent the rectangle wtht the # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return the string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", "str(self.__height) + ")"
        return (rect)
