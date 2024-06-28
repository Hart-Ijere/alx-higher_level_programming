#!/usr/bin/python3
"""
This script changes the name of the State object where id=2 to "New Mexico"
in the database hbtn_0e_6_usa.
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

    # Query for the State object with id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Check if the state exists
    if state_to_update:
        # Update the state's name
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
