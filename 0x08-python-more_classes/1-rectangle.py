#!/usr/bin/python3
class Rectangle:
    """this represents a rectangle"""
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
    """retrives the width atribute"""
    return self._width
@width.setter
def width(self, value):
    """set attribute"""
    if not isinstance
