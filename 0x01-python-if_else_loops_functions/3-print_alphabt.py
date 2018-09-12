#!/usr/bin/python3
for ltr in range(97, 123):
    if ltr not in [101, 113]:
        print("{:s}".format(chr(c)), end="")
