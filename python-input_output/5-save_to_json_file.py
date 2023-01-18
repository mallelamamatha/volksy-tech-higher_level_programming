#!/usr/bin/python3
'''str'''
import json


def save_to_json_file(my_obj, filename):
    '''file name'''
    with open(filename, "w") as myfile:
        return (myfile.write(json.dumps(my_obj)))
