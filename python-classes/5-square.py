#!/usr/bin/python3
"""class"""


class Square:
    """Printing a square"""
    def size(self):
        return self.__size

    def size(self, value):
        """constructor"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
      if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print('#', end="")
            print()
