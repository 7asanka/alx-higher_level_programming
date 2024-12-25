#!/usr/bin/python3
"""
Python file that contains the class definition of a City
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The City id of the class
        name (str): The City name of the class
        state_id (int): The state the city belongs to
    """

    __tablename__ = "cities"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
