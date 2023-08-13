#!/usr/bin/python3
"""class Amenity that inherits from BaseModel"""


from models.base_model import BaseModel



class Amenity(BaseModel):
    """Class that defines properties of Amenity.

    Attributes:
    name: string - empty string """


    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of Amenity.
        """
        super().__init__(*args, **kwargs)
