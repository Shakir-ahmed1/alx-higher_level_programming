#!/usr/bin/python3
""" sends a POST request and provides an email """
if __name__ == "__main__":
    from urllib import request, error
    from sys import argv
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
