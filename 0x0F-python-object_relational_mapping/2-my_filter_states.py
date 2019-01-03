#!/usr/bin/python3
""" takes in an arg and displays all values in * table of a db that match """

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
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id\
    ASC".format(argv[4]))
    states = cur.fetchall()
    for this_state in states:
        print(this_state)
    cur.close()
    usa_states.close()
