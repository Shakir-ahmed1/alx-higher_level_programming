#!/usr/bin/python3
""" prints all states in the state table """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

for r in session.query(State).all():
    print(f"{r.id}: {r.name}")
