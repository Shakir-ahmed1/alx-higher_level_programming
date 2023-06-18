#!/usr/bin/python3
""" fetches all states in the state table which start with N"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    db.query("SELECT * FROM states WHERE name REGEXP '^N.*$' ORDER BY states.id")
    r = db.store_result()
    for st in r.fetch_row(maxrows=0):
        print(st)
