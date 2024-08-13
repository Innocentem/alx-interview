#!/usr/bin/python3
"""
Function that rotates an nxn matrix 90 degrees clockwise
"""

def rotate_2d_matrix(matrix):
    """
    Rotates the given 2D matrix 90 degrees clockwise in place.

    :param matrix: List of lists representing the nxn matrix
    :type matrix: list of list of int
    :return: None (the matrix is modified in place)
    """
    
    # Get the number of rows (and columns) in the matrix
    n = len(matrix)
    
    # Transpose the matrix: swap matrix[i][j] with matrix[j][i]
    for i in range(n):
        for j in range(i, n):
            # Swap the elements at (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row of the matrix
    for i in range(n):
        matrix[i].reverse()
        
