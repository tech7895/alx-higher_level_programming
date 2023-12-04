#!/usr/bin/python3

"""This is myInt class module"""


class MyInt(int):
    """A MyInt class"""
    def __eq__(self, other):
        """This overides and inverts == operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """This verides and inverts != operator"""
        return int(self) == int(other)
