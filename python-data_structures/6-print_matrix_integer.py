#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        if len(x) == 0:
            print("")
        for i in range(len(x)):
            if i == len(x)-1:
                print("{:d}".format(x[i]))
            else:
                print("{:d} ".format(x[i]), end="")
