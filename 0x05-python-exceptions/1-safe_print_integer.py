#!/usr/bin/python3
def def safe_print_integer(value):
    if value != '\0':
        try:
            if not isinstance(value, int):
                raise ValueError
            else:
                print("{:d}".format(value))

        except ValueError:
            print("{} is not an integer".format(value))

        finally:
            if isinstance(value, int):
                return True
            else:
                return False
