#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    a = 0

    for i in argv[1:]:
        a += int(i)

    print("{:d}".format(a))
