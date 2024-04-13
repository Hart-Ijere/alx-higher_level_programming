#!/usr/bin/python3
"""
This module defines a class square
"""


class Square:
    """
    This class is a representation of a cla
    square.
    """

    def __init__(self, size=0):
        """
        Initialize a new instance.

        Args:
            size (int, optional): size of
            square.

        Raises:
            ValueError: If size is less
            than 0
            TypeError: If size is not an
            integer
        """

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be > 0")
        self.__size = size
