#!/usr/bin/python3
"""rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """matrix rotating"""

    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        matrix[i].reverse()
