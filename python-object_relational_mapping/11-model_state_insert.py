#!/usr/bin/python3
""" adds the State object Louisiana to the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_func():
    if (len(argv) != 4):
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print("{}".format(new.id))

    session.close()


if __name__ == "__main__":
    print_func()
