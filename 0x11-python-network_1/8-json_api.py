#!/usr/bin/python3
"""  Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter"""
if __name__ == "__main__":
    from sys import argv
    import requests
    q = argv[1] if len(argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, {'q': q})
    try:
        js = r.json()
        if js:
            print(f"[{js['id']}] {js['name']}")
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
