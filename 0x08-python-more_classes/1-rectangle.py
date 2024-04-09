#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle class with width and height attributes"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
