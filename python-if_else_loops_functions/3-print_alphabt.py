#!/usr/bin/python3
str = ""
for c in range(97, 123):
    if c != 101 and c != 113:
        str = str + chr(c)
print(f"{str}", end="")
