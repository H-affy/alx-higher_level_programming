#!/usr/bin/python3
"""defines a class rectangle that inherits from basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """initializes a new rectangle.

        Args:
        width (int): The width of the new rectangle
        height (int): The height of the new rectangle
        """

        super() .integer_validator("width", width)
        self.__width = width
        super() .integer_validator("height", height)
        self.__height = height

        def area(self):
            """return the area of the rectangle"""
            return self.__width * self.__height

        def __str__(self):
            """return the print() and str() representation of a rectangle"""
            string = "[" + str(self.__class__.__name__) + "] "
            string += str(self.__width) + "/" + str(self.__height)
            return (string)
