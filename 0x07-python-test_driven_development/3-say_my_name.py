#!/usr/bin/python3
"""
This is a module which comprises a function
prints full name

"""


def say_my_name(first_name, last_name=""):
    """ Prints "My name is <first name> <last name>"

    Parameters:
        first_name: the first name
        last_name: the last name

    Returns:
        No return

    Raises:
        TypeError: If the first_name or
        last_name is not a string


    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
