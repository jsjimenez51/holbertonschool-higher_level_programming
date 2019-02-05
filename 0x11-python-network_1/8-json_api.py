#!/usr/bin/python3
"""
takes in a letter and sends a POST to http://0.0.0.0:5000/search_user
"""
from requests import post
from sys import argv


if __name__ == "__main__":

    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]
    package = {'q': letter}
    req = post('http://0.0.0.0:5000/search_user', data=package)

    try:
        response = req.json()
        if len(response) == 0:
            raise KeyError()
    except KeyError:
        print("No result")
    except ValueError:
        print("Not a valid JSON")
    else:
        print("[{}] {}".format(response['id'], response['name']))
