#!/usr/bin/python3
def print_last_digit(number):
    ligit = number % 10
    if number < 0:
        ligit -= 10
    if ligit < 0:
        ligit *= -1
    print("{:d}".format(ligit), end="")
    return (ligit)
