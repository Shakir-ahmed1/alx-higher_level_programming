#!/usr/bin/python3
import MySQLdb
from sys import argv
db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
db.query('SELECT * FROM states')
r = db.store_result()
for st in r.fetch_row(maxrows=0):
    print(st)
