from app.models.user import User
from app.persistence.user_repository import UserRepository

class HBnBFacade:
    def __init__(self, user_repo=None):
        # إذا ما انرسل repo، أنشئ واحد تلقائي
        self.user_repo = user_repo if user_repo else UserRepository()

    def create_user(self, user_data):
        email = user_data['email'].strip().lower()

        if self.user_repo.get_by_attribute('email', email):
            raise ValueError("Email already registered")

        password = user_data.pop('password')

        user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=email,
            password=password,
            is_admin=user_data.get('is_admin', False)
        )

        self.user_repo.add(user)
        return user

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
