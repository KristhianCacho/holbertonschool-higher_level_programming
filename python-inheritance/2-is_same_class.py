#!/usr/bin/python3
# 2-is_same_class.py
# kristhian cacho
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class."""
    if type(obj) == a_class:
        return True
    return False
