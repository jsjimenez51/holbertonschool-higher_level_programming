#!/usr/bin/python3
"""
sends a search request to the Star Wars API
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    req = post('https://swapi.co/api/people', params={'search': argv[1]})
    try:
        response = r.json()
    except:
        print("Not a valid JSON")
    else:
        count = response['count']
        print("Number of results: {}".format(count))
        for item in response['results']:
            print(item['name'])
