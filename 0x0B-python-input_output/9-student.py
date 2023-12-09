#!/usr/bin/python3

"""This is a module defines a class Student"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This gets a dictionary representation of the Student"""
        return self.__dict__
