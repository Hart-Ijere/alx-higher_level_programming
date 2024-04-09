#!/usr/bin/python3

class Rectangle:
    """define a rectangle """

    
    def __init__(self, width=0, height=0):
        """initialize width and height """
        self._width = width
        seld._height = height
        
    @property
    def width(self):
        """retrieves value of width """
        return swlf._width

    @width.setter
    def width(self, value):
        """set value to width """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self._width = value


    @property
    def height(seld):
        """retrieve value of height """
        
        return self._height


    @height.setter
    def height(self, value):
        """set value of height. """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    
