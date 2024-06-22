#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa.

The script takes 3 arguments: MySQL username, MySQL password, and database
name. It connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys


def list_states_with_n(username, password, dbname):
    """
    Lists all states with a name starting with N from the database hbtn_0e_0_usa.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        dbname (str): The database name.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cursor = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE 'N%' "
             "ORDER BY id ASC")
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    list_states_with_n(username, password, dbname)
