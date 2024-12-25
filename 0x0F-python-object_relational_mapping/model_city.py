#!/usr/bin/python3
"""
python file that contains the class definition of
a City and an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class State(Base):
    """
    City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
        state_id (int): The state the city belongs to
    """

    __tablename__ = "cities"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
