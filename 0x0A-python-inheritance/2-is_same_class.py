#!/usr/bin/python3

"""This Checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """Returns true if object is an instance of the
    class, otherwise false
    """
    return (type(obj) == a_class)
