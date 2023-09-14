#!/usr/bin/python3


def print_last_digit(number):

    check = abs(number)
    check %= 10

    if check >= 0 and check <= 9:
        print("{:d}".format(check), end="")
        return(check)
    else:
        pass
