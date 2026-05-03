#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            uppercase_str = uppercase_str + chr(ord(c)-32)
        else:
            uppercase_str = uppercase_str + c
    print("{}".format(uppercase_str))
