#!/bin/bash

# Change working foler
cd "$(dirname "$0")"

# Delete: (local:remote)
#curl -s -X DELETE -H "Content-Type: application/json" -d "@json/state.delete.json" http://localhost:3000/states/delete
curl -s -X DELETE -H "Content-Type: application/json" -d "@json/state.delete.json" http://10.0.0.215:3000/states/delete