#!/usr/bin/python3
""" get states """
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import Base, State

    engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    st = State()
    st.name = "California"
    ct = City()
    ct.name = "San Francisco"
    st.cities.append(ct)
    session.add(st)
    session.add(ct)

    session.commit()
