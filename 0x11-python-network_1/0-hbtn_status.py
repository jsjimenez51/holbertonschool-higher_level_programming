#!/usr/bin/python3
"""
Fetches a website's info and displays it
"""
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen("https://intranet.hbtn.io/status") as response:
        content = response.read()
        lang = content.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content))
