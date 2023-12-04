#!/usr/bin/python3

"""Defines a class MyInt that inherits
from int."""


class MyInt(int):
    """This inverts int operators == and !=."""

    def __eq__(self, value):
        """This override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """This override != operator with == behavior."""
        return self.real == value
