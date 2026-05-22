#!/usr/bin/python3
"""Module 3"""


class Square:
    """Class defining a square - with calculation of area"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method returning the square area"""
        return self.__size ** 2
