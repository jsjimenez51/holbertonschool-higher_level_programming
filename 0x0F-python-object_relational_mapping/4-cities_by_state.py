#!/usr/bin/python3
""" lists all cities from db hbtn_0e_4_usa """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8")
    cur = db.cursor()
    cur.execute("Select cities.id, cities.name, states.name \
                FROM cities JOIN states \
                ON cities.state_id = states.id \
                ORDER BY cities.id ASC")
    cities_states = cur.fetchall()
    for row in cities_states:
        print(row)
    cur.close()
    db.close()
