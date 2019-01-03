#!/usr/bin/python3
""" takes in an a specific arg and safely lists it using the specified db """

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
    state_cities = "Select cities.name \
                    FROM cities \
                    JOIN states ON states.id = cities.state_id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC"
    cur.execute(state_cities, (argv[4],))
    this_state = cur.fetchall()
    print(", ".join([these_cities[0] for these_cities in this_state]))
    cur.close()
    db.close()
