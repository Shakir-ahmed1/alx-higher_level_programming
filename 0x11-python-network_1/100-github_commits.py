#!/usr/bin/python3
""" lists the last 10 commits of the given user"""
if __name__ == "__main__":
    import requests
    from sys import argv
    user = argv[2]
    repo = argv[1]
    url = f" https://api.github.com/repos/{user}/{repo}/commits"
    r = requests.get(url)
    js = r.json()
    if js:
        limit = 10 if len(js) > 10 else len(js)
        for j in range(limit):
            print(f"{js[j]['sha']}: {js[j]['commit']['author']['name']}")
