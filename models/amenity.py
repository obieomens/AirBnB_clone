#!/usr/bin/python3
""" Amenity class that inherits from BaseModel """
from models.base_model import BaseModel

class Amenity(BaseModel):
    """ for all amenities
    Attributes:
    name: string - empty string: this will be amenity name
    """
    name = ""
