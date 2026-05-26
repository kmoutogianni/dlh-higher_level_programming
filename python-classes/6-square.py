#!/usr/bin/python3
"""Module 6"""


class Square:
    """Class defining a square - with setter/getter"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Returns the position"""
        return self.__position

    @position.setter
    def position(self, position):
        """Sets the position"""
        if type(position) is tuple and len(position) == 2:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the square area"""
        return self.__size ** 2

    def my_print(self):
        """prints square on stdout"""
        if self.__size == 0:
            print()
        else:
            x_position = self.__position[0]
            for row in range(self.__size):
                if x_position > 0:
                    for x in range(x_position):
                        print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()
