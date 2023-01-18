#!/usr/bin/python3
'''str'''


def write_file(filename="", text=""):
    '''file name'''
    with open(filename, "w", encoding="UTF-8") as myfile:
        return(myfile.write(text))
