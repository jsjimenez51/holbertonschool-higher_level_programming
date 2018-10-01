#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ct = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
        except (ValueError, TypeError):
            continue
        else:
            ct += 1
    print()
    return (ct)
