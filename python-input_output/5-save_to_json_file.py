#!/usr/bin/python3
'''str'''


def save_to_json_file(my_obj, filename):
    '''file name'''
    with open(filename, mode="w") as myfile:
    json.dumps(my_obj, myfile)
