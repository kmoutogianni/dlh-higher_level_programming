#!/usr/bin/python3
"""Module Input Output"""
import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string"""

    return json.loads(my_str)
