#!/usr/bin/python3
"""Module Input Output"""


class Student:
    """class defining a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of Student"""
        return self.__dict__
