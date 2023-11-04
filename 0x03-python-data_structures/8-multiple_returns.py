#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character"""
    if sentence != '':
        first_char = sentence[0]
    else:
        first_char = None
    return (len(sentence), first_char)
