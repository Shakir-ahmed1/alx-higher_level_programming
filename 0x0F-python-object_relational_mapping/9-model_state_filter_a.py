#!/usr/bin/python3
""" lists all states that has a letter 'a' in them"""
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
    results = session.query(State).filter(State.name.like('%a%'))
    for r in results:
        print(f"{r.id}: {r.name}")
