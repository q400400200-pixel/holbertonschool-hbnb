from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt  # تاسك 4: استيراد JWT للتحقق من Admin
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Admin privileges required')
    @jwt_required()  # تاسك 4: يتطلب تسجيل دخول
    def post(self):
        """Register a new amenity"""
        current_user = get_jwt()  # تاسك 4: جلب معلومات المستخدم من JWT
        
        if not current_user.get('is_admin'):  # تاسك 4: التحقق من صلاحيات Admin
            return {'error': 'Admin privileges required'}, 403  # تاسك 4: خطأ 403 إذا مو Admin
        
        amenity_data = api.payload
        
        # تاسك 4: التحقق من عدم تكرار الاسم
        existing_amenity = facade.amenity_repo.get_by_attribute('name', amenity_data.get('name'))
        if existing_amenity:
            return {'error': 'Amenity already exists'}, 400
        
        try:
            new_amenity = facade.create_amenity(amenity_data)
            return new_amenity.to_dict(), 201
        except Exception as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):  # تاسك 4: endpoint عام - لا يحتاج تسجيل دخول
        """Retrieve a list of all amenities (public)"""
        amenities = facade.get_all_amenities()
        return [amenity.to_dict() for amenity in amenities], 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):  # تاسك 4: endpoint عام - لا يحتاج تسجيل دخول
        """Get amenity details by ID (public)"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        return amenity.to_dict(), 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(403, 'Admin privileges required')
    @api.response(400, 'Invalid input data')
    @jwt_required()  # تاسك 4: يتطلب تسجيل دخول
    def put(self, amenity_id):
        """Update an amenity's information"""
        current_user = get_jwt()  # تاسك 4: جلب معلومات المستخدم
        
        if not current_user.get('is_admin'):  # تاسك 4: التحقق من صلاحيات Admin
            return {'error': 'Admin privileges required'}, 403  # تاسك 4: خطأ 403 إذا مو Admin
        
        amenity_data = api.payload
        amenity = facade.get_amenity(amenity_id)
        
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        
        try:
            facade.update_amenity(amenity_id, amenity_data)
            return {"message": "Amenity updated successfully"}, 200
        except Exception as e:
            return {'error': str(e)}, 400
