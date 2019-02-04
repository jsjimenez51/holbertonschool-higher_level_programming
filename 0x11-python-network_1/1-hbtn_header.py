#!/usr/bin/python3
"""
takes in a URL, send it a request, then displays X-Request-Id
"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        print(response.info()['X-Request-ID'])
