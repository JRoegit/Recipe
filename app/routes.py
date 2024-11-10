import base64
from flask import Blueprint, jsonify, render_template
from .db import *

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return jsonify(message="Welcome")

@main_bp.route('/createrecipe')
def about():
    return render_template('createrecipe.html')

@main_bp.route('/recipe/<int:recipe_id>',methods=['GET'])
def recipe_page(recipe_id):
    recipe = fetch_recipe(recipe_id)
    
    encoded_image = base64.b64encode(recipe['photo']).decode('utf-8')
    image_src = f"data:image/jpeg;base64,{encoded_image}"

    return render_template('recipe.html',image_src=image_src)