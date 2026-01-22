"""
In-memory repository for storing objects temporarily
This will be replaced with a database in Part 3
"""
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass
    
    @abstractmethod
    def get(self, obj_id):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def update(self, obj_id, data):
        pass
    
    @abstractmethod
    def delete(self, obj_id):
        pass
    
    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository:
    """Repository for storing objects in memory"""
    
    def __init__(self):
        self._storage = {}
    
    def add(self, obj):
        """Add an object to the repository"""
        self._storage[obj.id] = obj
    
    def get(self, obj_id):
        """Get an object by ID"""
        return self._storage.get(obj_id)
    
    def get_all(self):
        """Get all objects"""
        return list(self._storage.values())
    
    def update(self, obj_id, data):
        """Update an object"""
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
        return obj
    
    def delete(self, obj_id):
        """Delete an object"""
        if obj_id in self._storage:
            del self._storage[obj_id]
            return True
        return False
    
    def get_by_attribute(self, attr_name, attr_value):
        """Get an object by a specific attribute"""
        return next(
            (obj for obj in self._storage.values() 
             if getattr(obj, attr_name, None) == attr_value),
            None
        )


class UserRepository(InMemoryRepository):
    """Repository specifically for User objects"""
    pass
