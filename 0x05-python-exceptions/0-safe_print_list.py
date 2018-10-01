#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ct = 0

    for num in range(x):
        try:
            print("{}".format(my_list[num]), end="")
        except IndexError:
            print()
            return (ct)
        else:
            ct += 1
    print()
    return (ct)
