#!/usr/bin/python3
"""
sends a request to the URL and displays the value of X-Request-Id
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    req = get(argv[1])
    print(req.headers.get('X-Request-Id'))
