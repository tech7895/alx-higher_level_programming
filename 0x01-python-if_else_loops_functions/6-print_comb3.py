#!/usr/bin/python3

"""Prints all possible different combinations of two digits in ascending order"""

for dgt1 in range(0, 10):
    for dgt2 in range(dgt1 + 1, 10):
        if dgt1 == 8 and dgt2 == 9:
            print("{}{}".format(dgt1, dgt2))
        else:
            print("{}{}".format(dgt1, dgt2), end=", ")
