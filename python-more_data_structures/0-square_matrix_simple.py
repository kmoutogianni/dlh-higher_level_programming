#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        """ for every row in the original matrix,
        create a new row with the squared values of its elements """
        new_row = []
        for element in row:
            new_row.append(element**2)
        new_matrix.append(new_row)
    return new_matrix
