#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=database, port=3306)
    cursor = db.cursor()

    # Create SQL query using format to match state name
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}'"
             " ORDER BY id ASC".format(state_name))

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
