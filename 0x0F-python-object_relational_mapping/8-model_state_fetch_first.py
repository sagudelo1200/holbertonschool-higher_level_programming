#!/usr/bin/python3
"""[script that prints the first State object from the database hbtn_0e_6_usa]
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    host = 'localhost'
    user = argv[1]
    psw = argv[2]
    db = argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(user, psw, host, db),
        pool_pre_ping=True
    )
    session = sessionmaker(bind=engine)()

    first_state = session.query(State).order_by(State.id.asc()).first()

    if first_state:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print('Nothing')
