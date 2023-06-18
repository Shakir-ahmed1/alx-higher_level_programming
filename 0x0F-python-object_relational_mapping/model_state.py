#!/usr/bin/python3
""" a base module that creates a python state object from db"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


class State(Base):
    """ defines the state table """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
