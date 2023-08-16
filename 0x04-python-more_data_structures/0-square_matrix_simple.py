#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    """A function that computes the square value of
    all in integers of a matrix
    """

    new_list = []
    if len(matrix) == 0:
        return new_list

    new_list = [[i*i for i in j] for j in matrix]
    return new_list
