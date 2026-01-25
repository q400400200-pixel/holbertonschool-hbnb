#!/usr/bin/python3
from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity  # تاسك 3: استيراد JWT للمصادقة
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()  # تاسك 3: يتطلب تسجيل دخول لإنشاء تقييم
    def post(self):
        """Create a new review"""
        current_user = get_jwt_identity()  # تاسك 3: جلب معرف المستخدم من JWT
        data = api.payload
        
        data['user_id'] = current_user  # تاسك 3: تعيين المستخدم تلقائياً
        
        place = facade.get_place(data['place_id'])
        if not place:
            return {'error': 'Place not found'}, 404
        
        if place.owner.id == current_user:  # تاسك 3: منع تقييم المكان الخاص
            return {'error': 'You cannot review your own place'}, 400  # تاسك 3: خطأ 400 للمكان الخاص
        
        existing_reviews = facade.get_reviews_by_place(data['place_id'])
        for review in existing_reviews:
            if review.user.id == current_user:  # تاسك 3: منع التقييم المكرر
                return {'error': 'You have already reviewed this place'}, 400  # تاسك 3: خطأ 400 للتقييم المكرر
        
        try:
            review = facade.create_review(data)
            return review.to_dict(), 201
        except Exception as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):  # تاسك 3: endpoint عام - لا يحتاج تسجيل دخول
        """Get all reviews (public endpoint)"""
        reviews = facade.get_all_reviews()
        return [r.to_dict() for r in reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):  # تاسك 3: endpoint عام - لا يحتاج تسجيل دخول
        """Get review details (public endpoint)"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return review.to_dict(), 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Invalid input data')
    @jwt_required()  # تاسك 3: يتطلب تسجيل دخول لتعديل التقييم
    def put(self, review_id):
        """Update a review"""
        current_user = get_jwt_identity()  # تاسك 3: جلب المستخدم الحالي
        review = facade.get_review(review_id)
        
        if not review:
            return {'error': 'Review not found'}, 404
        
        if review.user.id != current_user:  # تاسك 3: التحقق من الملكية - فقط صاحب التقييم يقدر يعدل
            return {'error': 'Unauthorized action'}, 403  # تاسك 3: خطأ 403 إذا ما كان صاحب التقييم
        
        data = api.payload
        try:
            facade.update_review(review_id, data)
            return {'message': 'Review updated successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 400

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized action')
    @jwt_required()  # تاسك 3: يتطلب تسجيل دخول لحذف التقييم
    def delete(self, review_id):
        """Delete a review"""
        current_user = get_jwt_identity()  # تاسك 3: جلب المستخدم الحالي
        review = facade.get_review(review_id)
        
        if not review:
            return {'error': 'Review not found'}, 404
        
        if review.user.id != current_user:  # تاسك 3: التحقق من الملكية - فقط صاحب التقييم يقدر يمسح
            return {'error': 'Unauthorized action'}, 403  # تاسك 3: خطأ 403 إذا ما كان صاحب التقييم
        
        deleted = facade.delete_review(review_id)
        if not deleted:
            return {'error': 'Review not found'}, 404
        return {'message': 'Review deleted successfully'}, 200
