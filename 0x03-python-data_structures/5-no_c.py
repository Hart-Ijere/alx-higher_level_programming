#!/usr/bin/python3
def no_c(my_string):
    updated_str = ''
    for s in my_string:
        if s != 'c' and s != 'C':
            updated_str += s
    return (updated_str)
