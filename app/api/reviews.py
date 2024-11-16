from flask import *
from app.data.reviews import *

review_bp = Blueprint('review', __name__)

@review_bp.route('/review/<int:recipe_id>',methods=['POST'])
def add_review(recipe_id):
    # Will want to fetch this from cookies once user and session is set up.
    user_id = session.get('user_id')
    print(user_id)
    if user_id:
        data = request.form.to_dict()
        print("creating review...")
        success = create_review(recipe_id,user_id,data)
        if not success:
            flash('Something went wrong.')
    else:
        flash('Must be signed in to submit a review.')
    return redirect(url_for("main.recipe_page", recipe_id=recipe_id))
    
@review_bp.route('/review/<int:recipe_id>', methods=['GET'])
def get_reviews(recipe_id):
    reviews = fetch_reviews(recipe_id)
    return reviews, 200
    
