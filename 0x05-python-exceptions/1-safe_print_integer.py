#!/usr/bin/python3
def safe_print_integer(value):
    if value != '\0':
        try:
            if isinstance(value, int):
                print("{:d}".format(value))

        except TypeError:
            print("{} is not an integer".format(value))

        finally:
            if isinstance(value, int):
                return True
            else:
                return False
            
        
