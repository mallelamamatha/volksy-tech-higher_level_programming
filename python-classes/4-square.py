#!/usr/bin/python3
"""class"""


class Square:
    """ Access and update private attribute"""
    def __init__(self, size=0):
    self.size = size
    def size(self):
        """constructor"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        """area of square"""
        return (self.__size * self.__size)
