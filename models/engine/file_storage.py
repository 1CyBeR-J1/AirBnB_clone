#!/usr/bin/python3
"""Module that contains the FileStorage class"""

import json
import os.path

class FileStorage:
    """serializes instances to a JSON file and deserializes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__,
            obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        with open(self.__file_path, mode="w") as f:
            d_storage = {}
            for key, value in self.__objects.items():
                d_storage[key] = value.to_dict()
            json.dump(d_storage, f)

    def classes(self):
        """Returns a dict of classes and their values"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                "BaseModel": BaseModel,
                "User:": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review}
        return classes



    def reload(self):
        """
        deserializes the JSON file to (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the
        file doesn’t exist, no exception should be raised)
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                dfile = json.load(f)
                dfile = {k: self.classes()[v["__class__"]](**v)
                        for k, v in dfile.items()}
                self.__objects = dfile
        else:
            return
