#!/usr/bin/python3

"""This module containing the function
from_json_string"""
import json


def from_json_string(my_str):
    """This returns an object (Python data structure)

    Args:
        my_str (str): json object to convert to Python object.

    Returns:
        type: Python object.
    """
    # print("type json.loads(my_str)--> {}".format(type(json.loads(my_str))))
    # print("type my_str--> {}".format(type(my_str)))
    return json.loads(my_str)
