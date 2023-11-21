#!/usr/bin/python3
"""defines a magic class from a given bytecode"""
import math


class MagicClass:
    """initializes MagicClass"""
    def __init__(self, radius=0):
        """initializes the data"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

        def area(self):
            """calculating the area"""
            return self._MagicClass__radius ** 2 * math.pi

        def circumference(self):
            """calculating the circumference"""
            return 2 * math.pi * self._MagicClass__radius
