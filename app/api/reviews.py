from flask import Blueprint, jsonify, redirect, request, url_for
from app.data.reviews import *

review_bp = Blueprint('review', __name__)

@review_bp.route('/review/<int:recipe_id>',methods=['POST'])
def add_review(recipe_id):
    # Will want to fetch this from cookies once user and session is set up.
    user_id = 1
    data = request.form.to_dict()
    success = create_review(recipe_id,user_id,data)
    # TODO Should return a redirect
    if success:
        return redirect(url_for(f"/recipe/{recipe_id}"))
    else:
        return {"error : failed to create review"}, 400
    
@review_bp.route('/review/<int:recipe_id>', methods=['GET'])
def get_reviews(recipe_id):
    reviews = fetch_reviews(recipe_id)
    return reviews, 200
    
