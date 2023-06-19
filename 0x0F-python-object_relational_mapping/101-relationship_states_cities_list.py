#!/usr/bin/python3
""" get states """
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all()
    count = 0
    for s in result:
        print(f"{s.id}: {s.name}")
        for c in s.cities:
            print(f"\t{c.id}: {c.name}")
