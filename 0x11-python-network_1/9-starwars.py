#!/usr/bin/python3
"""
sends a search request to the Star Wars API
"""
from requests import post
from sys import argv


if __name__ == "__main__":

    if len(argv) == 1:
        char = ""
    else:
        char = argv[1]

    package = {'search': char}

    try:
        req = get('https://swapi.co/api/people/?', params=package)
        response = req.json()
        results = response['results']
        count = response['count']
        print("Number of results: {}".format(count))
        for item in results:
            print(item['name'])
    except Exception as err:
        print(err)
