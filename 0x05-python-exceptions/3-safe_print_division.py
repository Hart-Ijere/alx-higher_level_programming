#!/usr/bin/python3
def safe_print_division(a, b):

    myResult = 0
    try:
        myResult = a / b
        return myResult
    except ZeroDivisionError:
        pass
        return None
    except TypeError:
        pass
    finally:
        print("Inside result: {:}".format(myResult))
