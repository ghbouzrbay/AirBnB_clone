#!/usr/bin/python3
"""Defines a class FileStorage."""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Class that serializes instances to a JSON file and deserializesJSON file to instances.
     Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Creates new instances of class."""
        pass

    def all(self):
        """Returns the dictionary objects.

        Returns:
            dict: objects.
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (any): object.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        objct_dict = {}

        for key, value in FileStorage.__objects.items():
            objct_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(objct_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects only if the JSON file __file_path exists;
                                                                       otherwise do nothing;"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = file.read()
        except Exception:
            return
        objects = eval(data)
        for (key, value) in objects.items():
            objects[key] = eval(key.split('.')[0] + '(**value)')
        self.__objects = objects

    def delete(self, obj):
        """Deletes obj from __objects"""
        try:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            del self.__objects[key]
            return True
        except Exception:
            return False

