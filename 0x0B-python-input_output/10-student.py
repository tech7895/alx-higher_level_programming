#!/usr/bin/python3

'''
Classes:
-> Student
'''


class Student:
    ''' A student class '''

    def __init__(self, first_name, last_name, age):
        '''A constructor method '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' The method that returns directory description with filter '''

        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            res = {}
            for i in attrs:
                if i in self.__dict__:
                    res[i] = self.__dict__[i]
            return res
        return self.__dict__
