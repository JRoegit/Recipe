import base64
from flask import *
# from flask import Blueprint, jsonify, render_template, request
from .data.users import *
from .data.recipes import *
from .data.reviews import *

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return jsonify(message="Welcome")

@main_bp.route('/createrecipe')
def about():
    return render_template('createrecipe.html')

@main_bp.route('/signin', methods=['GET','POST'])
def signin_page():
    if request.method == 'POST':
        formData = request.form.to_dict()
        userExists = check_user_exists(formData['username'])
        if userExists:
            user = fetch_user_by_username(formData['username'])
            if user['password'] == formData['password']:
                print(f'correct password, user id is: {user['user_id']}')
                session['user_id'] = user['user_id']
                session['username'] = user['username']
                return redirect(url_for('main.home'))
            else:
                flash("Incorrect username or password")
    return render_template('signin.html')

@main_bp.route('/signup', methods=['GET','POST'])
def signup_page():
    if request.method == 'POST':
        formData = request.form.to_dict()
        userExists = check_user_exists(formData['username'])
        if userExists :
            flash("user already exists")
        else:
            create_user(formData)
            return redirect(url_for('main.signin_page'))
    return render_template('signup.html')

@main_bp.route('/recipe/<int:recipe_id>',methods=['GET'])
def recipe_page(recipe_id):
    recipe = fetch_recipe(recipe_id)
    reviews = fetch_reviews(recipe_id)
    if recipe:
        recipeAuthor = fetch_user(recipe['user_id'])
        ingredients = get_ingredients(recipe['recipe_id'])
        directions = get_directions(recipe['recipe_id'])
        encoded_image = base64.b64encode(recipe['photo']).decode('utf-8')

        image_src = f"data:image/jpeg;base64,{encoded_image}"

        del recipe['photo']
        print(recipe)
        return render_template('recipe.html',recipe=recipe, ingredients=ingredients, directions=directions, recipeAuthor=recipeAuthor,image_src=image_src, recipe_id=recipe_id, reviews=reviews)
    else:
        return render_template('recipe.html')