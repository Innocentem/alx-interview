#!/usr/bin/python3
"""
Function that rotates nxn matrix 90 degrees clockwise
"""
def rotate_2d_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()

