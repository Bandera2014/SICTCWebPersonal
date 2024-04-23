#!/bin/bash
 
# Change working folder
cd "$(dirname "$0")"
 
# Get Account: (local:remote)
curl -s -X GET http://localhost:3000/accounts/2 | jq .
#curl -s -X GET http://raspberrypi-ip:3000/accounts/2 | jq .

