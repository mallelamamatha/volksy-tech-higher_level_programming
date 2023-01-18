#!/usr/bin/python3
'''str'''


def read_file(filename=""):
    '''file name'''
    with open(filename, "r", encoding="UTF-8") as myfile:
        print(myfile.read(), end="")
