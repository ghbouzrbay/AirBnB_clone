#!/usr/bin/python3
"""Defines a class Base"""
<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
>>>>>>> f714a04ce707fa504ba7d2516befd2466130f9e1
>>>>>>> 90b0560b5e966e0a16f17ce918b0372320b6ad0f
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
<<<<<<< HEAD
        Returns:
            str: class details"""
        str_vari = "["
        str_vari += str(self.__class__.__name__) + '] ('
        str_vari += str(self.id) + ') ' + str(self.__dict__)
        return str_vari
=======
>>>>>>> f714a04ce707fa504ba7d2516befd2466130f9e1

        Returns:
            str: class details
        """
        string_vari = "["
        string_vari += str(self.__class__.__name__) + '] ('
        string_vari += str(self.id) + ') ' + str(self.__dict__)
        return string_vari

    def save(self):
        """Update public instance attribute updated_at with current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ of
        the instance.

        Returns:
            dict: key/value pairs.
        """
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj

