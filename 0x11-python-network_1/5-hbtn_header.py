#!/usr/bin/python3
""" Response header using requests """
if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers["X-Request-Id"])
