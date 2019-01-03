#!/usr/bin/python3
"""
lists all State that contain the letter a in the db
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()

    a_states =\
    Session.query(State).filter(State.name.contains('a')).order_by(State.id)
    for state in a_states:
        print("{}: {}".format(state.id, state.name))

    Session.close()
