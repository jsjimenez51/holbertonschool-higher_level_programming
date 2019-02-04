#!/bin/bash
# a script that sends a request to a URL that displays its status code
curl -sw '%{http_code}' -o /dev/null "$1"
