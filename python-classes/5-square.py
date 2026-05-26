#!/usr/bin/python3
"""Module 5"""


class Square:
    """Class defining a square - with setter/getter"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Returns the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the square area"""
        return self.__size ** 2

    def my_print(self):
        """prints square on stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
