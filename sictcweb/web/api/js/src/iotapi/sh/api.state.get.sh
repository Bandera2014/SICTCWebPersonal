#!/bin/bash

# Change working foler
cd "$(dirname "$0")"

# Get State: (local:remote)
#curl -s -X GET http://localhost:3000/states/1 | jq .
curl -s -X GET http://10.0.0.215:3000/states/1 | jq .