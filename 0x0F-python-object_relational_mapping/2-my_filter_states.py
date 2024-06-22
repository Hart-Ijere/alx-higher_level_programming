#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

The script takes 4 arguments: MySQL username, MySQL password, database name,
and state name searched. It connects to a MySQL server running on localhost at
port 3306. Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys


def find_state_by_name(username, password, dbname, state_name):
    """
    Displays all values in the states table where name matches the argument.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        dbname (str): The database name.
        state_name (str): The state name to search for.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]
    find_state_by_name(username, password, dbname, state_name)
