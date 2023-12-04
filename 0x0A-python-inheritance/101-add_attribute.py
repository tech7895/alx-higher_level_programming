#!/usr/bin/python3

"""this module defines a function that adds
attributes to objects"""


def add_attribute(obj, att, value):
    """This adds a new attribute to an
	object if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
