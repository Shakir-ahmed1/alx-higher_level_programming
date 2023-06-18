#!/usr/bin/python3
""" fetchs the first element """
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
    r = session.query(State).first()
    if r is not None:
        print(f'{r.id}: {r.name}')
    else:
        print("Nothing")
