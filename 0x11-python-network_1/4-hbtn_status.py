#!/usr/bin/python3
"""
fetches content from the holberton intranet
"""
from requests import get


if __name__ == "__main__":
    req = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
