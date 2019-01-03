#!/usr/bin/python3
""" Defines a function that lists all states from db hbtn_0e_0_usa """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

# Connects Python MySQL modlule to the db
    select_states = MySQLdb.connect(host="localhost",
                                    port=3306,
                                    user=argv[1],
                                    passwd=argv[2],
                                    db=argv[3],
                                    charset="utf8")
# Creates a cursor to utilize this particular connection
    cur = select_states.cursor()
# Executes the query from Python
    cur.execute("SELECT * FROM states ORDER BY id ASC")
# Fetch and print all at once
    states = cur.fetchall()
    for row in states:
        print(row)
# Clean up
    cur.close()
    select_states.close()
