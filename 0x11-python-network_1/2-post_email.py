#!/usr/bin/python3
""" sends a POST request and provides an email """
from urllib import request, parse
from sys import argv
email = {'email': argv[2]}
data = parse.urlencode(email)
data = data.encode('ascii')
req = request.Request(argv[1], data)
with request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
