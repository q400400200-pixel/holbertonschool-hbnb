from app.models.user import User
from app.persistence.repository import UserRepository

class HBnBFacade:
    def __init__(self, user_repo=None):
        # إذا ما انرسل repo، أنشئ واحد تلقائي
        self.user_repo = user_repo if user_repo else UserRepository()
    
    def create_user(self, user_data):
        """Create a new user with hashed password"""
        # Normalize email
        email = user_data['email'].strip().lower()
        
        # Check if email already exists
        if self.user_repo.get_by_attribute('email', email):
            raise ValueError("Email already registered")
        
        # Create user (password will be hashed in __init__)
        user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=email,
            password=user_data['password'],
            is_admin=user_data.get('is_admin', False)
        )
        
        # Add user to repository
        self.user_repo.add(user)
        
        return user
    
    def get_all_users(self):
        """Get all users"""
        return self.user_repo.get_all()
    
    def get_user_by_email(self, email):
        """Get user by email"""
        # Normalize email for search
        normalized_email = email.strip().lower()
        return self.user_repo.get_by_attribute('email', normalized_email)
    
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        return self.user_repo.get(user_id)
