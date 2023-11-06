#!/usr/bin/python3
"""Define an inherited list class Mylist"""

class MyList(list):
    """Implement sorted printing of in buitl list class"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
