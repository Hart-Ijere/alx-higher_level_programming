#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
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
            username, password, database), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    # Query for all State objects with a name containing 'a'
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    # Delete each state in the result set
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
