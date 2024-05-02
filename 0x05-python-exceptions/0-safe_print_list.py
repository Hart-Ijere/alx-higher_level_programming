#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        if isinstance(x, int):
            for i in my_list:
                print(i, end='')
            print()  # Print a newline after printing all elements
            return len(my_list)  # Return the length of my_list
        else:
            raise ValueError("x is not an integer")
    except ValueError as e:
        print(e)  # Print the error message if x is not an integer

