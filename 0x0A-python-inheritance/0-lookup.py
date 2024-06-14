#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        List of attributes and methods available for the object.
    """
    return dir(obj)

