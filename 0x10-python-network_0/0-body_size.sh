#!/bin/bash
# takes in a URL and sends a request to display the size of the body of the URL
curl -sI "$1" | grep "Content-Length" | cut -d ' ' =f2
