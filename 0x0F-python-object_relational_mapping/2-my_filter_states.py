#!/usr/bin/python3
""" takes in an arg and displays all values in * table of a db that match """

if __name__ == '__main__':
    import MySQLdb
    import sys

    usa_states = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3],
                                 charset="utf8")
    cur = usa_states.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY \'{}\' ORDER BY id\
    ASC".format(sys.argv[4]))
    states = cur.fetchall()
    for this_state in states:
        print(this_state)
    cur.close()
    usa_states.close()
