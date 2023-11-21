#!/usr/bin/python3

"""This defines a class Square"""


class Square:
    """This represents a square
    Attributes:
        __size (int): the size of a side of the square
    """
    def __init__(self, size=0):
        """This initializes the square
        Args:
            size (int): the size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """This calculates the square's area
        Returns:
            area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")

            else:
                self.__size = value
