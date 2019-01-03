#!/usr/bin/python3
"""
prints the first State object from a given db
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

    first_state = Session.query(State).order_by(State.id).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    Session.close()
