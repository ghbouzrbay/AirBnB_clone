#!/usr/bin/python3
"""class Amenity that inherits from BaseModel"""


from models.base_model import BaseModel



class Amenity(BaseModel):
    """Class that defines properties of Amenity.

    Attributes:
    name: string - empty string """


    name = ""

    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        """ constructor method """
        super().__init__(self, *args, **kwargs)
=======
        """Creates new instances of Amenity.
        """
        super().__init__(*args, **kwargs)
>>>>>>> b4daca4802fd4a1550b7230df0f14bcc3965b3f9
