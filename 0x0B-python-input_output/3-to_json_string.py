#!/usr/bin/python3
"""Returns the JSON rep of an object"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
