#!/usr/bin/env python3
"""
BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    """ The main class for the models"""
    
    def __init__(self):
        """Initialize the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()
    
    def update(self, data):
        """
        Update object attributes from a dictionary

    Args:
        data (dict): Dictionary containing updated values
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
    
    def to_dict(self):
        """Convert object attributes to a dictionary"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
