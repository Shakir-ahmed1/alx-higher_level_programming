#!/bin/bash
# Make a request to the server
curl -s -X PUT 0.0.0.0:5000/catch_me -L -d "user_id=98" -H "Origin: HolbertonSchool" -H "Referer: HolbertonSchool" -H "Content-Type: application/json" -d "{\"user_id\": 98}" -H "Expect: " -H "Transfer-Encoding: " -H "Connection: close"

