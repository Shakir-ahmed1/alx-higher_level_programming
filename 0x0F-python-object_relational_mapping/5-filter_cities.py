#!/usr/bin/python3
""" gets cities of the given state"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""
    SELECT c.name
    FROM states s JOIN cities c ON c.state_id = s.id
    WHERE s.name = '{}'
            """.format(argv[4]))
    result = []
    for d in cur.fetchall():
        result.append(d[0])
    print(", ".join(result))
