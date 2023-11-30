#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        a = 1 / a
        b = -b

    res = 1
    for i in range(b):
        res *= a

    return res
