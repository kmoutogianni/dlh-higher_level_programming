#!/usr/bin/python3
"""Module 1 More Classes"""


class Rectangle:
    """Class defining a rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
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
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
