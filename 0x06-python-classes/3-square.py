#!/usr/bin/python3
"""
This module contains the definition of a class
"""


class Square:
    """
    This is the representation of a class
    """

    def __init__(self, size=0):
        """
        Initialize a new instance of the square class
        

        Args:
            size (int, optional): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must >= 0")
        self.__size = size


        def area(self):
            """
            Calculates the area of a square.

            Returns:
                int: The area of a square.
            """
            return self.__size ** 2
