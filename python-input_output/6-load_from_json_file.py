#!/usr/bin/python3
'''str'''
import json


def load_from_json_file(filename):
    '''file name'''
    with open(filename, "w") as myfile:
        return json.load(myfile)
