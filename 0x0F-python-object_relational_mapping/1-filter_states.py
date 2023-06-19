#!/usr/bin/python3
""" fetches all states in the state table which start with N"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%'")
    for r in cur.fetchall():
        print(r)
    db.close()
