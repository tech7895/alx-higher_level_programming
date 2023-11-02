#!/usr/bin/python3

def magic_calculation(a, b):
    """This program matches bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for k in range(4, 6):
            c = add(c, k)
        return (c)

    else:
        return(sub(a, b))
