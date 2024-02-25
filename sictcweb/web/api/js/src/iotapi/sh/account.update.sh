#!/bin/bash
 
# Change working folder
cd "$(dirname "$0")"
 
# Update Account Test: (local:remote)
curl -s -X POST -H "Content-Type: application/json" -d "@json/account.update.json" http://localhost:3000/accounts/update
#curl -s -X POST -H "Content-Type: application/json" -d "@json/account.update.json" http://raspberrypi-ip:3000/accounts/update

