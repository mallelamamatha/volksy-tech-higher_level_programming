#!/usr/bin/python3
'''str'''


def append_write(filename="", text=""):
    '''file name'''
    with open(filename, mode="a", encoding="UTF-8") as myfile:
        return (myfile.write(text))
