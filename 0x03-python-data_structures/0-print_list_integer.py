#!/usr/bin/python3
def print_list_integer(my_list=[]):

    """Prints all integer of a list"""

    for list_item in range(len(my_list)):
        print("{:d}".format(my_list[list_item]))
