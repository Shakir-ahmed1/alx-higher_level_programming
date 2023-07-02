#!/usr/bin/python3
""" sends a POST request and provides an email """
import urllib.request
import urllib.parse
from sys import argv
email = {'email': argv[2]}
data = urllib.parse.urlencode(email)
data = data.encode('ascii')
req = urllib.request.Request(argv[1], data)
with urllib.request.urlopen(req) as response:
    print(response.read())
