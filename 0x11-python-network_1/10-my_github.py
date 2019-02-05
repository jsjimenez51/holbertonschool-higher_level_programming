#!/usr/bin/python3
"""
takes users Github credentials and access the GIthub API to display id
"""
from request import get
from sys import argv


if __name__ == '__main__':

    try:
        req = get('https://api.github.com/user', auth=(argv[1], argv[2]))
        print(req.json()['id'])
    except:
        print("None")
