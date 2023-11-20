#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ This  function that prints x elements of a list """
    tot = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            tot += 1
        except IndexError:
            break
    print()
    return(tot)
