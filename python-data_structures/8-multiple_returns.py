#!/usr/bin/python3

def multiple_returns(sentence):
    len_sentence = len(sentence)
    if len_sentence > 0:
        first_char = sentence[0]
    else:
        first_char = None
    return (len_sentence, first_char)
