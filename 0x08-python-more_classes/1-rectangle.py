#!/usr/bin/python3


class Rectangle:
    """define a rectangle """

    
    def __init__(self, width=0, height=0):
        """initialize width and height """
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """retrieves value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """set value to width """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """retrieve value of height """
        
        return self.__height


    @height.setter
    def height(self, value):
        """set value of height. """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    
