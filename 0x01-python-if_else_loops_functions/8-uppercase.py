#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        if ord('a') <= ord(ch) <= ord('z'):
            uper = chr(ord(ch) - ord('a') + ord('A'))
        else:
            uper = ch
        print("{}".format(uper), end="")
    print()
