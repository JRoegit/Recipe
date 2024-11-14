from flask import Blueprint, jsonify, request
from app.data.recipes import *

recipes_bp = Blueprint('recipes', __name__)

@recipes_bp.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = fetch_recipes()
    return recipes, 200

@recipes_bp.route('/recipes/<int:recipe_id>',methods=['GET'])
def get_recipe(recipe_id):
    recipe = fetch_recipe(recipe_id)
    if recipe:
        return recipe, 200
    else:
        return {"error" : "Recipe does not exist"}, 404 

@recipes_bp.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.get_json()
    result = create_recipe(data)
    if result:
        return result , 201
    else:
        return {"error" : f"user_id {data.get('user_id')} does not exist"}, 404

@recipes_bp.route('/recipes/<int:recipe_id>', methods=['PUT'])
def modify_recipe(recipe_id):
    result = update_recipe(request.get_json(), recipe_id)
    return result, 201

@recipes_bp.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    result = remove_recipe(recipe_id)
    print(result)
    if result:
        return result, 200
    else:
        return {"error" : "Recipe does not exist"}, 404 
    
@recipes_bp.route('/recipes/form', methods=['POST'])
def recipe_form():
    form = request.form.to_dict()
    image = request.files['photo'].read()

    success = create_recipe_form(form,image,1)
    if success:
        return form, 201
    else:
        return {"error" : "Something went wrong."}, 400
