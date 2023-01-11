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


