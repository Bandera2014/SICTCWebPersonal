#!/bin/bash

# Change working foler
cd "$(dirname "$0")"

# Update State Test: (local:remote)
#curl -s -X POST -H "Content-Type: application/json" -d "@json/state.update.json" http://localhost:3000/states/update
curl -s -X POST -H "Content-Type: application/json" -d "@json/state.update.json" http://10.0.0.215:3000/states/update