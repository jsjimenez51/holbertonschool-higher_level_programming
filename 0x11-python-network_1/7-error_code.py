#!/usr/bin/python3
"""
sends a request to a URL and displays the body of the response
"""
from requests import get
from requests.exceptions import HTTPError
from sys import argv


if __name__ == "__main__":
    req = get(argv[1])
    try:
        req.raise_for_status()
    except:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
