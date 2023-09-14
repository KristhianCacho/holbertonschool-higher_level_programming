#!/usr/bin/python3
for i in range(0, 10):
    for a in range(1, 10):
        if i == a or i == 9:
            a += 1
        elif i >= a:
            a += 1
        elif i == 8 and a == 9:
            print("{}{}".format(i, a))
        else:
            print("{}".format(i), end="")
            print("{}, ".format(a), end="")
