#!/usr/bin/python3
"""
sends a POST request to the passed URL with the provided email
displays the body of the response
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    req = post(argv[1], data={'email': argv[2]})
    print(req.text)
