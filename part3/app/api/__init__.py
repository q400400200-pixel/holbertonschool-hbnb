from flask import Blueprint
from flask_restx import Api

api_v1_bp = Blueprint('api_v1', __name__)
api = Api(api_v1_bp, title="HBnB API", version="1.0", doc="/docs")

# استيراد namespaces
from app.api.v1.users import api as users_ns
from app.api.v1.protected import api as protected_ns

# تسجيل namespaces
api.add_namespace(users_ns, path="/users")
api.add_namespace(protected_ns, path="/protected")
