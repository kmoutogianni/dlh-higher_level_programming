#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """ Takes a Python Dictionary with data
    and the the filename of the output JSON file"""
    #  Your code here to serialize and save data to the specified file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """returns a Python Dictionary
    with the deserialized JSON data from the file"""
    # Your code here to load and deserialize data from the specified file
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
