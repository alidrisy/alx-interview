#!/usr/bin/python3
""" Model for rotate_2d_matrix function """


def rotate_2d_matrix(matrix: list) -> None:
    """ Rotate an n x n 2D matrix 90 degrees clockwise. """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
