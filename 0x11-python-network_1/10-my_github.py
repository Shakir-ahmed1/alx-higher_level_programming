#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    from sys import argv
    username = argv[1]
    password = argv[2]
    url = f"https://api.github.com/users/{username}"
    hd = {"Authorization": password, "X-GitHub-Api-Version": "2022-11-28"}
    r = requests.get(url, headers= hd)
    js = r.json()
    print(js['id'])
