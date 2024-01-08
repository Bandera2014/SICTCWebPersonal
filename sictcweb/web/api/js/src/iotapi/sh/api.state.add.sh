#!/bin/bash

# Change working foler
cd "$(dirname "$0")"

# Add: (local:remote)
#curl -s -X POST -H "Content-Type: application/json" -d "@json/state.add.json" http://localhost:3000/states/add | jq .
curl -s -X POST -H "Content-Type: application/json" -d "@json/state.add.json" http://10.0.0.215:3000/states/add | jq .