#!/usr/bin/python3
"""class"""


class Square:
    """ Access and update private attribute"""
    def size(self):
        """constructor"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        slef.__size = size

    def __init__(self, size=0):
        """constructor"""
        slef.__size = 0

    def area(self):
        """area of square"""
        return (self.__size * self.__size
