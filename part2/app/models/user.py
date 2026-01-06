"""
User model
"""
from app.models.base_model import BaseModel

class User(BaseModel):
    """User class for managing user data"""
    
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
    
    def to_dict(self):
        """Convert user to dictionary"""
        return {
            **super().to_dict(),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin
        }
