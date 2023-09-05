#!/usr/bin/python3
"""the script define a square printing function"""


def print_square(size):
    """
    print a square with the # character

    Args:
    size (int): The height/width of the square

    Raise:
    TypeError: if the size is not an integer
    ValueError: if size is < 0
    """
    if isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for jin range(size)]
        print("")
