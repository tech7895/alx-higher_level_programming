#!/usr/bin/python3

"""This defines a square-printing function"""


def print_square(size):
    """Prints a square with the # character

    Args:
        size (int): The height/width
    Raises:
        TypeError: If size is not integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
