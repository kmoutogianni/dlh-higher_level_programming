#!/usr/bin/python3
"""Module 1 More Classes"""


class Rectangle:
    """Class defining a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """allows print() and str() to print rectangle with the character #"""
        rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return rectangle

        for h in range(self.__height):
            for w in range(self.__width):
                rectangle = rectangle + "#"
            if h != self.__height - 1:
                rectangle = rectangle + "\n"
        return rectangle

        def __repr__(self):
            return "Rectangle({}, {})".format(self.__width, self.__height)
