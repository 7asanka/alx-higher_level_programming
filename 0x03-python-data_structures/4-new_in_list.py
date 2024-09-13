#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    cpy_list = [i for i in my_list]
    if idx < 0:
        return cpy_list
    if idx > len(my_list):
        return cpy_list

    cpy_list[idx] = element

    return cpy_list
