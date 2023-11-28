#!/usr/bin/python3

"""A function that defines a locked class"""


class LockedClass:
    """
    Prevents the user from instantiating new LockedClass attributes
    for anything but the attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
