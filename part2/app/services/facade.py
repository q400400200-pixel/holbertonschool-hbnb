"""
Facade pattern implementation
Acts as an interface between the API and business logic
"""
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    """Facade class to manage interactions between layers"""
    
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
    
    # User operations
    def create_user(self, user_data):
        """Create a new user"""
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    
    def get_user(self, user_id):
        """Get a user by ID"""
        return self.user_repo.get(user_id)
    
    def get_all_users(self):
        """Get all users"""
        return self.user_repo.get_all()
    
    def update_user(self, user_id, user_data):
        """Update a user"""
        return self.user_repo.update(user_id, user_data)
    
    def get_user_by_email(self, email):
        """Get a user by email"""
        return self.user_repo.get_by_attribute('email', email)
    
    # Amenity operations
    def create_amenity(self, amenity_data):
        """Create a new amenity"""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity
    
    def get_amenity(self, amenity_id):
        """Get an amenity by ID"""
        return self.amenity_repo.get(amenity_id)
    
    def get_all_amenities(self):
        """Get all amenities"""
        return self.amenity_repo.get_all()
    
    def update_amenity(self, amenity_id, amenity_data):
        """Update an amenity"""
        return self.amenity_repo.update(amenity_id, amenity_data)
    
    # Place operations
    def create_place(self, place_data):
        """Create a new place"""
        place = Place(**place_data)
        self.place_repo.add(place)
        return place
    
    def get_place(self, place_id):
        """Get a place by ID"""
        return self.place_repo.get(place_id)
    
    def get_all_places(self):
        """Get all places"""
        return self.place_repo.get_all()
    
    def update_place(self, place_id, place_data):
        """Update a place"""
        return self.place_repo.update(place_id, place_data)
    
    # Review operations
    def create_review(self, review_data):
        """Create a new review"""
        review = Review(**review_data)
        self.review_repo.add(review)
        
        # Add review to place
        place = self.get_place(review.place_id)
        if place:
            place.add_review(review.id)
        
        return review
    
    def get_review(self, review_id):
        """Get a review by ID"""
        return self.review_repo.get(review_id)
    
    def get_all_reviews(self):
        """Get all reviews"""
        return self.review_repo.get_all()
    
    def get_reviews_by_place(self, place_id):
        """Get all reviews for a specific place"""
        return [review for review in self.review_repo.get_all() 
                if review.place_id == place_id]
    
    def update_review(self, review_id, review_data):
        """Update a review"""
        return self.review_repo.update(review_id, review_data)
    
    def delete_review(self, review_id):
        """Delete a review"""
        return self.review_repo.delete(review_id)
