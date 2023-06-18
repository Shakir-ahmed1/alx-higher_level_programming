#!/usr/bin/python3
""" add a new state """
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    up = session.query(State).filter(State.id == 2).one_or_none()
    if up is not None:
        up.name = "New Mexico"
        session.commit()
