#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the FileStorage class."""
=======
""" FileStorage class that serializes instances to a JSON file and deserializes JSON file to instances"""
>>>>>>> 2eb5c8e2ea76d054a51b193ab5c882889c839416
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
<<<<<<< HEAD
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
=======
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by <class name>.id
>>>>>>> 2eb5c8e2ea76d054a51b193ab5c882889c839416
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
<<<<<<< HEAD
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj._class.name_
=======
        """Return dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
>>>>>>> 2eb5c8e2ea76d054a51b193ab5c882889c839416
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
<<<<<<< HEAD
                    cls_name = o["_class_"]
                    del o["_class_"]
=======
                    cls_name = o["__class__"]
                    del o["__class__"]
>>>>>>> 2eb5c8e2ea76d054a51b193ab5c882889c839416
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
