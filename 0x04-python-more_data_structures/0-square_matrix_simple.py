#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for x in matrix:
        square.append(list(map(lambda x: x**2, x)))
        return (square)
