#!/usr/bin/python3
def islower(c):
    """ check for a lower case character.

    Args:
    c(chr) alphabet to be checked.
    """
    if ord(c) in range(97,123):
        print("{} is lower".format(c))
    else:
        print("{} is upper".format(c))
