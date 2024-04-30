#!/usr/bin/python3
def def safe_print_integer(value):
    if value != '\0':
        try:
            print("{:d}".format(int(value)))
            return True

        except TypeError:
            print("{} is not an integer".format(value))
            return False
        
