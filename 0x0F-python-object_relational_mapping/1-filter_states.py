#!/usr/bin/python3
""" Lists all states with a name starting with N from the db hbtn_0e_0_usa """

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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    N_states = cur.fetchall()
    for state in N_states:
        print(state)
    cur.close()
    usa_states.close()
