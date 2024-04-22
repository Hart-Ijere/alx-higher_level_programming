#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file and prints to the stdout.

    Args:
        filename (str): text file to be printed.

    Return:
        (str): a text file
    """
    with open("filename", "r") as fd:
        read_data = fd.read()
        print(read_data)
