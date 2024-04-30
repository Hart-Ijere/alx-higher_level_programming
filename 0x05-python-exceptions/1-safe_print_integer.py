#!/usr/bin/python3
def def safe_print_integer(value):
    if value != '\0':
        try:
            print("{:d}".format(value))

        except TypeError:
            print("{} is not an integer".format(value))

        finally:
            if isinstance(value, int):
                return True
            else:
                return False
