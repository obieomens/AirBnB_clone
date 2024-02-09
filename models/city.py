#!/usr/bin/python3
""" City  class that inherits from BaseModel """
from models.base_model import BaseModel

class City(BaseModel):
    """ for city with public attributes:
    Attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string: it will be the city name
    """
    state_id = ""
    name = ""
