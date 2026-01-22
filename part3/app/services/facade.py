from app.models.user import User
from app.persistence.repository import UserRepository

class HBnBFacade:
    def __init__(self, user_repo=None):
        self.user_repo = user_repo if user_repo else UserRepository()
    
    def create_user(self, user_data):
        """Create a new user with hashed password"""
        email = user_data['email'].strip().lower()
        
        if self.user_repo.get_by_attribute('email', email):
            raise ValueError("Email already registered")
        
        user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=email,
            password=user_data['password'],
            is_admin=user_data.get('is_admin', False)
        )
        
        self.user_repo.add(user)
        return user
    
    def get_all_users(self):
        """Get all users"""
        return self.user_repo.get_all()
    
    def get_user_by_email(self, email):
        """Get user by email"""
        normalized_email = email.strip().lower()
        return self.user_repo.get_by_attribute('email', normalized_email)
    
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        return self.user_repo.get(user_id)

# Create a single instance
facade = HBnBFacade()
