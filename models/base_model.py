#!/usr/bin/python3
"""A module that contains the Base class"""

import uuid
from datetime import datetime
from models import storage

class BaseModel():
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """string representation of the base class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """updates the inst attr updated_at with the curr datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary of __dict__ of the instance"""
        my_dct = self.__dict__.copy()
        my_dct["__class__"] = self.__class__.__name__
        my_dct["created_at"] = my_dct["created_at"].isoformat()
        my_dct["updated_at"] = my_dct["updated_at"].isoformat()
        return my_dct
