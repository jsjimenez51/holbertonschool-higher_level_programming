#!/usr/bin/python3
def no_c(my_string):
    new_st = ''
    for ltrs in my_string:
        if ltrs not in ['c', 'C']:
            new_st += ltrs
    return new_st
