#!/usr/bin/python3

def safe_print_division(a, b):

    myResult = 0

    try:
        if not isinstance((a, b), int):
            raise TypeError
    except TypeError:
        print("Ooops! yoi entered an invalid number")
    except ZeroDivisionError:
        print("a and b must be integers")

    finally:
        if b > 0:
            myResult = a / b
            print("Inside reseult: {}".format(myResult))
            return myResult
        
        else;
            myWord = "None"
            print("Inside result: {}".format(myWord)
            return None
        
