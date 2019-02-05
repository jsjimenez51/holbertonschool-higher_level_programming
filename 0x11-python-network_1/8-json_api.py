#!/usr/bin/python3
"""
takes in a letter and sends a POST to http://0.0.0.0:5000/search_user
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    if argv[1] is None:
        q = ""
    else:
        q = argv[1]
    req = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        response = req.json()
    except:
        print("Not a valid JSON")
    else:
        if response:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
