#!/bin/bash
# gets content size of the response
curl -s "$1" | wc -c
