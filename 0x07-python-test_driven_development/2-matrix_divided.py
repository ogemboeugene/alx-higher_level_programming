#!/usr/bin/python3
"""
Divides all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not a number.
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is equal to 0.

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])

    new_matrix = []
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix of integers/floats")

            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix
