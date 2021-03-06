#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response
handles errors and prints out the HTTP status code
argv[1]: URL
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
