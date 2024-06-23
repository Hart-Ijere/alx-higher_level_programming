#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.

The script takes 4 arguments: MySQL username, MySQL password, database name,
and state name. It connects to a MySQL server running on localhost at port
3306. Results are sorted in ascending order by cities.id.
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, dbname, state_name):
    """
    Lists all cities of a given state from the database hbtn_0e_4_usa.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        dbname (str): The database name.
        state_name (str): The name of the state.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cursor = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cursor.close()
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]
    list_cities_by_state(username, password, dbname, state_name)
