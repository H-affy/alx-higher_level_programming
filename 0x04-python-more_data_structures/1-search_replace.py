#!/usr/bin/python3
def search_replace(my_list, search, replace):

    """Replaces all occurence of an element by another
    in a new list
    """

    if len(my_list) == 0:
        return my_list

    new_list = [elem if elem != search else replace for elem in my_list]
    return new_list
