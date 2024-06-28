#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a' from the
database hbtn_0e_6_usa.
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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    # Query all State objects that contain the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    # Print the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
