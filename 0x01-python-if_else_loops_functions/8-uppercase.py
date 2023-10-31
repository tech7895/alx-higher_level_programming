#!/usr/bin/python3

def uppercase(str):
    """This function prints a string in uppercase."""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print("")
