#!/usr/bin/python3
"""Define rectangle"""

class Rectangle:
    """This represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing the rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self._width

    @width.setter
    def width(self, value):
        """Set attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

