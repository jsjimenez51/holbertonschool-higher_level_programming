#!/bin/bash
# sends a JSON POST request to a URL on port 5000
curl -sX POST "$1" -d "@$2" --header "Content-Type: application/json"
