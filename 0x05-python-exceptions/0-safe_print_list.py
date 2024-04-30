#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''Prints x elements of a list'''
    try:
        count = 0
        for item in my_list:
            if count < x:
                print(item, end=' ')
                count += 1
            else:
                break  # Stop printing once x elements are printed
    except TypeError:
        print("An error occurred while printing the list")

    finally:
        return count
