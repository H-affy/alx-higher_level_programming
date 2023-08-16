#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    new_dirs = a_dictionary.copy()
    lists_key = list(new_dirs.keys())

    for i in lists_key:
        new_dirs[i] *= 2

    return (new_dirs)
