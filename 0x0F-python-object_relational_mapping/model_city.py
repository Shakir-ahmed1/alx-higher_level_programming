#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))

