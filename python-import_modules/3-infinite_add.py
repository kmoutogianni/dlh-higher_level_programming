#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum_args = 0
    for i in range(1, len(sys.argv)):
        sum_args = sum_args + int(sys.argv[i])
    print("{}".format(sum_args))
