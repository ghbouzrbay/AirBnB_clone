#!/usr/bin/python3
"""class City that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class that defines properties of City.

    Attributes:
         state_id: string - empty string: it will be the State.id
         name: string - empty string """


state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of City."""
        super().__init__(*args, **kwargs)

