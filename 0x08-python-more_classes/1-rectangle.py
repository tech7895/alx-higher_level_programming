#!/usr/bin/python3
"""This class defines a rectangle"""


class Rectangle:
    """this class represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle class
        Args:
            width: This represents the width of the rectangle
            height: This represents the height of the rectangle
        Raises:
            TypeError: if the size is not integer
            ValueError: if the size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
