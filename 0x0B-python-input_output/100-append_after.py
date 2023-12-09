#!/usr/bin/python3

"""This module 100-append_after
Inserts a line of text to a file,
after each line containing specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """This appends the new_string after
    the search_string in filename.
    Args:
        - filename: name of the file
        - search_string: string to append after
        - new_string: the new_string to append
    """

    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
