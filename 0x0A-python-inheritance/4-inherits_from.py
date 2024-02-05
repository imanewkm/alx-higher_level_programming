#!/usr/bin/python3
"""Determines if the object is an instance or not"""


def inherits_from(obj, a_class):
    """Determine if the obj is an instance of a sub class

    Args:
        obj (any): The object to check.
        a_class (type): the class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
