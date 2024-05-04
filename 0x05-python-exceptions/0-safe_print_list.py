#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count_item = 0
    
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            count_item += 1
    except IndexError:
        print("\nOnly", count_items, "elements were printed because the list is shorter.")
    print()
    return count_item 


