#!/bin/bash
# prints the status code only while curling
curl -s -o /dev/null -w "%{http_code}" "$1"
