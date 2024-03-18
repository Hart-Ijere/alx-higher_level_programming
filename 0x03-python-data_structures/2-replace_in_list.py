#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lengthOfList = len(my_list)
    if idx < 0 or idx >= lengthOfList:
        return my_list
    my_list[idx] = element
    return my_list
