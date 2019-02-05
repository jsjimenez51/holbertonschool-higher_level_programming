#!/usr/bin/python3
"""
takes users Github credentials and access the GIthub API to display id
"""
from request import get
from sys import argv


if __name__ == '__main__':

    user = argv[1]
    pwd = argv[2]
    try:
        req = get('https://api.github.com/user', auth=(user, pwd))
        print(req.json()['id'])
    except:
        print("None")
