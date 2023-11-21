#!/usr/bin/python3
"""defines aclass square"""


class square:
    """represents a square"""

    def __init__(self, size=0):
        """initializes a new square.

        Args:
        size (int): size of the new square.
        """
        self.size = size

        @property
        def size(self):
            """"get/set the current size of the square"""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an interger")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """return the current area of the square"""
                return (self.__size ** 2)
