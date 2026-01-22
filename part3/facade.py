from app.models.user import User
from app.persistence.storage import storage

class HBnBFacade:

    def create_user(self, data):
        user = User(**data)
        storage.new(user)
        storage.save()
        return user

    def get_user_by_email(self, email):
        users = storage.all(User).values()
        for user in users:
            if user.email == email:
                return user
        return None

    def authenticate_user(self, email, password):
        user = self.get_user_by_email(email)
        if user and user.check_password(password):
            return user
        return None
