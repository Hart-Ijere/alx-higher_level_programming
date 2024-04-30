#!/usr/bin/python3

def countList(my_list=[]):
    '''Count items in a list'''
    if not my_list:
        return 0
    else:
        count = 0
        for i in my_list:
            count += 1
    return count

def safe_print_list(my_list=[], x=0):
    '''Prints the correct number of elements in a list'''
    item_cnt = countList(my_list)

    try:
        for i in my_list:
            if item_cnt != x:
                raise ValueError
            else:
                print(i, end=' ')

    except ValueError:
        print("Number passed to x does not match number of items in the list")

    finally:
        return item_cnt

    
