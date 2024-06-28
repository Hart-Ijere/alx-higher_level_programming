#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
and prints the new state's id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine and connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    # Create new State object “Louisiana”
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()
