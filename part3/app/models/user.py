from werkzeug.security import generate_password_hash, check_password_hash
import uuid

class User:
    def __init__(self, email, password, first_name=None, last_name=None):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
