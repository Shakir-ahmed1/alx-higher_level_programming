#!/bin/bash
# sends json Post request to the given url
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
