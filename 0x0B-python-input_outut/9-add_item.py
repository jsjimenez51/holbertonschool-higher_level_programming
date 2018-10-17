#!/usr/bin/python3
"""
Module that contains a functiona that adds all argurments to a Python list
and then saves that list to a file
"""
from sys import argv


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    newList = load_from_json_file(filename)
except (FileNotFoundError, BaseException):
    newList = []
for item in argv[1:]:
    newList.append(item)
save_to_json_file(newList, filename)
