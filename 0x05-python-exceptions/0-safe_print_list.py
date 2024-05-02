#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        if isinstance(x, int)
        return x
    except ValueError:
        print("x is not an integer")
    except TypeError:
        print("x is not an integer")
    finally:
        for i in my_list:
            print(i)

