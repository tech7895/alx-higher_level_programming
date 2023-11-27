#!/usr/bin/python3
"""This class defines a rectangle"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes this rectangle class
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        Raises:
            TypeError: size is not integer
            ValueError: size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """This returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """This presents a diagram of the rectangle
        defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
