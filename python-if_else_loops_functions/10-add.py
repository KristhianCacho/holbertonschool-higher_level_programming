#!/usr/bin/python3


def add(a, b):

    # Add validations just for fun and learn, exercise expect error
    checkA = isinstance(a, int)
    checkB = isinstance(b, int)

    if (checkA and checkB) == 1:
        return(a + b)
    else:
        return(a + b)
