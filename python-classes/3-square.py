#!/usr/bin/python3
"""class"""


class Square:
    """square size"""
    def __init__(self, size=0):
        """constuctor"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area of a square"""
        return (self.__size * self.__size)
