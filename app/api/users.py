from flask import Blueprint, jsonify, request
from app.data.users import *

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = fetch_users()
    return users, 200

@users_bp.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    user = fetch_user(user_id)
    print(user)
    if user:
        return user, 200
    else:
        return {"error" : "user does not exist"}, 404 

@users_bp.route('/users', methods=['POST'])
def add_user():
    result = create_user(json.loads(request.get_data()))
    return result , 201

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    result = update_user(request.get_json())
    return result, 201

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = remove_user(user_id)
    print(result)
    if result:
        return result, 200
    else:
        return {"error" : "user does not exist"}, 404 