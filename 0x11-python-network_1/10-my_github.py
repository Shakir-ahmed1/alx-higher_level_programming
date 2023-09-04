#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username and
    password) and uses the GitHub API to display your id """
if __name__ == "__main__":
    import requests
    from sys import argv
    username = argv[1]
    password = argv[2]
    url = f"https://api.github.com/user"
    r = requests.get(url, auth=(username, password))
    js = r.json()
    print(js['id'] if r.status_code != 401 else None)
