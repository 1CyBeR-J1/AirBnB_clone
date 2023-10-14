#!/usr/bin/python3
"""Module that contains the City class"""

from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherits BaseModel"""
    state_id = ""
    name = ""
