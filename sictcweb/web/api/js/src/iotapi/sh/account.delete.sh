 
#!/bin/bash
 
# Change working folder
cd "$(dirname "$0")"
 
# Delete: (local:remote)
curl -s -X DELETE -H "Content-Type: application/json" -d "@json/account.delete.json" http://localhost:3000/accounts/delete/:id
#curl -s -X DELETE -H "Content-Type: application/json" -d "@json/account.delete.json" http://raspberrypi-ip:3000/accounts/delete/:id

