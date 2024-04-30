#!/usr/bin/python3

def countList(myList):
    count = 0
    for i in myList:
        count += 1
    return count
		
def safe_print_list(my_list=[], x=0):
    if my_list:
    try:
        if x == countList(my_list):
	    for i in my_list:
	        print(i, end=' ')
				
    except ValueError:
        print("item mismatch")
    finally:
        return x

