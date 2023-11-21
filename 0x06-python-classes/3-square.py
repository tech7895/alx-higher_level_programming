#!/usr/bin/python3

# 0-square.py by Odoi Leonard
"""This is a module that defines a square """


class Square:

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: This represnets the size of the square defined
        Raises:
            TypeError: size is not integer
            ValueError: the size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        This calculates the area of the square
        Returns: the size
        """

        return (self.__size ** 2)
