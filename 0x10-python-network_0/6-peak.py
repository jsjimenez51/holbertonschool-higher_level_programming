#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds peak using a binary search
    """
    if list_of_integers:
        start = 0
        end = len(list_of_integers) - 1
        if start == end:
            return list_of_integers[start]
        # checks if the start or end of the list are peaks
        if list_of_integers[start] > list_of_integers[1]:
            return list_of_integers[start]
        if list_of_integers[end] > list_of_integers[end - 1]:
            return list_of_integers[end]
        # finds the mid point of the list to begin binary search
        mid = (end - start) // 2
        if list_of_integers[mid] < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[:mid])
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            return find_peak(list_of_integers[mid + 1:])
        return list_of_integers[mid]
    return None
