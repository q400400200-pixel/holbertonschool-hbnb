import bcrypt
from app import create_app

app = create_app()
with app.app_context():
    from app.models.user import User
    u = User.query.first()
    print("Email:", u.email)
    print("admin123:", bcrypt.checkpw(b"admin123", u.password.encode()))
    print("Admin123!", bcrypt.checkpw(b"Admin123!", u.password.encode()))
    print("admin1234:", bcrypt.checkpw(b"admin1234", u.password.encode()))