#!/usr/bin/python3
'''str'''


def write_file(filename="", text=""):
    '''filename'''
    with open(filename, "w", enclosing="UTF-8") as myfile:
        print(myfile.write(), end="")