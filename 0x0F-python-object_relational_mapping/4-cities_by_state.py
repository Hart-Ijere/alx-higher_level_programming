#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.

The script takes 3 arguments: MySQL username, MySQL password, and database
name. It connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id.
"""

import MySQLdb
import sys


def list_all_cities(username, password, dbname):
    """
    Lists all cities from the database hbtn_0e_4_usa.

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
    query = "SELECT * FROM cities ORDER BY id ASC"
    cursor.execute(query)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    list_all_cities(username, password, dbname)
