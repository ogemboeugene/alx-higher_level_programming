#!/usr/bin/python3
"""
Prints a square with the character '#'.
"""


def print_square(size):
    """
    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.
    """
    # if not isinstance(size, int):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
