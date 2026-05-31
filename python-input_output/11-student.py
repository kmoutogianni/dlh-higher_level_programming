#!/usr/bin/python3
"""Module Input Output"""


class Student:
    """class defining a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of Student"""

        if type(attrs) is list:
            """If attrs is list of strings, return dictionary containing
            only attributes contained in this list"""
            attr_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    attr_dict[attr] = self.__dict__[attr]
            return attr_dict

        return self.__dict__

    def reload_from_json(self, json):
        """replaces all self attributes from json dictionary """
        self.__dict__.update(json)
