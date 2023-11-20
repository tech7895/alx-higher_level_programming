#!/usr/bin/python3

def safe_print_resultision(a, b):
    """This returns the resultision of a by b."""
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
