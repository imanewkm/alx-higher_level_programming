#!/usr/bin/python3
"""the object is instance or instance of a class"""


def is_kind_of_class(obj, a_class):
    """Defines the nature of an object.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance - True
        If not - False
    """
    if isinstance(obj, a_class):
        return True
    return False
