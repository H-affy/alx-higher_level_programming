#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    lists_ord = list(a_dictionary.keys())
    lists_ord.sort()

    for i in lists_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
