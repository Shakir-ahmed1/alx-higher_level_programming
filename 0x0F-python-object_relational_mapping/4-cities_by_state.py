#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute('SELECT c.id, c.name, s.name FROM states s JOIN cities c ON c.state_id = s.id')
    cities = cur.fetchall()
    print(len(cities))
    for b in cities:
        print(b)
    cur.close()
    db.close()
