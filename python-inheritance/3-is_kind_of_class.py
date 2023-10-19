#!/usr/bin/python3
# 3-is_kind_of_class.py
# kristhian cacho
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class."""
    if isinstance(obj, a_class):
        return True
    return False
