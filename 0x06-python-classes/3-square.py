#!/usr/bin/python3
"""defines a class square"""


class square:
    """represents a square"""

    def __int__(self, size=0):
        """initializes anew square.

        Args:
        size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """return the current area of the square."""
            return (self.__size * self.__size)
