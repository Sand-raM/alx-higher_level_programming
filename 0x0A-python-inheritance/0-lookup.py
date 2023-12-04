#!/usr/bin/python3
"""Defines an object attribute lookup function."""



def lookup(obj):
    """Returns a lists of the object's available attributes."""
    return (dir(obj))
