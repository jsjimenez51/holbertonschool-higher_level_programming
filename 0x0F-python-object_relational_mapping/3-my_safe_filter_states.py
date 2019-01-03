#!/usr/bin/python3
""" takes in an arg and displays all values in * table of a db that match and
is safe from injections """
# sets placeholders for the db to fill in data values safely

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    usa_states = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3],
                                 charset="utf8")
    cur = usa_states.cursor()
    grab_state = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(grab_state, (argv[4],))
    states = cur.fetchall()
    for this_state in states:
        print(this_state)
    cur.close()
    usa_states.close()
