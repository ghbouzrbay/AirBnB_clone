#!/usr/bin/python3
"""Defines a class Base"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """ Class that defines properties of base """

    def __init__(self, *args, **kwargs):
        """ Creates new instances of Base """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for (key, value) in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns a string represation of class details.

        Returns:
            str: class details"""
        string_vari = "["
        string_vari += str(self.__class__.__name__) + '] ('
        string_vari += str(self.id) + ') ' + str(self.__dict__)
        return string_vari

    def save(self):
        """Update public instance attribute updated_at with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ of
        the instance.

        Returns:
            dict: key/value pairs.
        """
        objct_dict = self.__dict__.copy()
        objct_dict['__class__'] = self.__class__.__name__
        objct_dict['created_at'] = self.created_at.isoformat()
        objct_dict['updated_at'] = self.updated_at.isoformat()
        return objct_dict
