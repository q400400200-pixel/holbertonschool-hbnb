#!/usr/bin/env python3
"""
User API endpoints
"""
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity  # تاسك 3: استيراد JWT للمصادقة
from app.services.facade import facade

api = Namespace('users', description='User operations')

# User model for input validation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email address'),
    'password': fields.String(required=True, description='Password')
})

# تاسك 3: نموذج جديد للتعديل (بدون email و password)
user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(description='First name'),
    'last_name': fields.String(description='Last name')
})

@api.route('/')
class UserList(Resource):
    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Get all users"""
        users = facade.get_all_users()
        return [user.to_dict() for user in users], 200
    
    @api.expect(user_model)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Invalid input')
    def post(self):
        """Register a new user"""
        user_data = api.payload
        
        try:
            new_user = facade.create_user(user_data)
            
            return {
                'id': new_user.id,
                'message': 'User successfully created'
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

@api.route('/<user_id>')
@api.param('user_id', 'The user identifier')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user_by_id(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return user.to_dict(), 200
    
    # تاسك 3: endpoint جديد لتعديل بيانات المستخدم
    @api.expect(user_update_model)
    @api.response(200, 'User updated successfully')
    @api.response(404, 'User not found')
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Invalid input')
    @jwt_required()  # تاسك 3: يتطلب تسجيل دخول
    def put(self, user_id):
        """Update user information"""
        current_user = get_jwt_identity()  # تاسك 3: جلب المستخدم الحالي
        
        if user_id != current_user:  # تاسك 3: التحقق - المستخدم يعدل بياناته فقط
            return {'error': 'Unauthorized action'}, 403  # تاسك 3: خطأ 403 إذا حاول تعديل بيانات غيره
        
        user_data = api.payload
        
        if 'email' in user_data or 'password' in user_data:  # تاسك 3: منع تعديل email و password
            return {'error': 'You cannot modify email or password'}, 400  # تاسك 3: خطأ 400 لتعديل email/password
        
        user = facade.get_user_by_id(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        
        try:
            facade.update_user(user_id, user_data)
            return {'message': 'User updated successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 400
