#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""
                SELECT cities.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %s
                ORDER BY cities.id
    """, (argv[4],))
    rows = cur.fetchall()

    print(", ".join([rows[0] for i in rows]))
    cur.close()
    db.close()
