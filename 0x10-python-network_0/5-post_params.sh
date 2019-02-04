#!/bin/bash
# sends a POST request to the passed URL that displays the body of response
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST $1
