#!/usr/bin/python3
def best_score(a_dictionary):
    # function that returns the key with the biggest integer value
    highest_scoring = None
    if a_dictionary is not None:
        highest_score = 0
        for key, value in a_dictionary.items():
            if value > highest_score:
                highest_score = value
                highest_scoring = key
    return highest_scoring
