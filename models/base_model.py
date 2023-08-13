#!/usr/bin/python3
"""Defines a class Base"""


from uuid import uuid4
from datetime import datetime
from models import storage
import uuid
import json
import sys
import os.path

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
        """print in "[<class name>] (<self.id>) <self.__dict__>" format"""

        return ('[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__class__.__dict__))


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
