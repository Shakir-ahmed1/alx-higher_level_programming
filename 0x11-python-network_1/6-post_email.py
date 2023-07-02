#!/usr/bin/python3
""" Post an email using requests"""
if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    email = argv[2]
    r = requests.post(url, {"email": email})
    print(r.text)
