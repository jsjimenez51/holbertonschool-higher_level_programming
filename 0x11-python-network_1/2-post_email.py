#!/usr/bin/python3
"""
sends a POST request to the passed URL with the passed email
argv[1]: URL
argv[2]: email
"""
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    content = urlencode({'email': argv[2]}).encode('utf-8')
    with urlopen(argv[1], content) as response:
        print(response.read().decode('utf-8'))
