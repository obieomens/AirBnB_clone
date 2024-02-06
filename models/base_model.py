#!/usr/bin/python3
""" class BaseModel that defines all common
attributes/methods for other classes """
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ BaseModel of the HBnB project """
    def __init__(self, *args, **kwargs):
        """ Initialization
        Args:
        *args : Unused
        **kwargs: Key/value pairs of attributes
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for z, v in kwargs.items():
                if z == "created_at" or z == "updated_at":
                    self.__dict__[z] = datetime.strptime(v, tform)
                else:
                    self.__dict__[z] = v
                
            else:
                models.storage.new(self)

        def save(self):
            """ update updated_at: datetime, where datetime is current datetime"""
            self.updated_at = datetime.today()
            models.storage.save()

            def to_dict(self):
                """ dictionary of the BaseModel instance 
                with key/value pair __class__ representing
                object class name
                """

                rdict = self.__dict__.copy()
                rdict["created_at"] = self.created_at.isoformat()
                rdict["updated_at"] = self.updated_at.isoformat()
                rdict["__class__"] = self.__class__.__name__
                return rdict

            def __str__(self):
                """ Return print or string representation of BaseModel instance """
                clname = self.__class__.__name__
                return "[{}] ({}) {}".format(clname, self.id, self.__dict__)


