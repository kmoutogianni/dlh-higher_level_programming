#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # returns a new dictionary with all values multiplied by 2
    new_dictionary = {}
    keys = a_dictionary.keys()
    for key in keys:
        multiplied_value = a_dictionary[key] * 2
        new_dictionary[key] = multiplied_value  # adds key and value
    return new_dictionary
