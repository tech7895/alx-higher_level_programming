#!/usr/bin/python3

"""This is a module that defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """This creates a Python object from a given JSON file"""
    with open(filename) as f:
        return json.load(f)
