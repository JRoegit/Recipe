from flask import Blueprint, jsonify, request
from app.db import *

review_bp = Blueprint('review', __name__)

@review_bp.route('/review/<int:recipe_id>',methods=['POST'])
def add_review(recipe_id):
    # Will want to fetch this from cookies once user and session is set up.
    user_id = 1

    data = request.form.to_dict()
    image = request.files['photo'].read()

    success = create_review(recipe_id,user_id,image,data)
    if success:
        return data, 201
    else:
        return {"error : failed to create review"}, 400
    
@review_bp.route('/review', methods=['GET'])
def get_reviews():
    reviews = fetch_reviews()
    return reviews, 200
    