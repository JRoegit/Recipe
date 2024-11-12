from .utils import *
import json
from datetime import datetime

def fetch_recipes():
    conn, cursor = get_db_connection(True)
    recipes = cursor.execute("SELECT * FROM RECIPES").fetchall()
    conn.close()
    return recipes

def fetch_recipe(recipe_id):
    conn, cursor = get_db_connection(True)
    recipe = cursor.execute(f"SELECT * FROM RECIPES WHERE recipe_id = {recipe_id}").fetchone()
    conn.close()
    return recipe

def create_recipe(data):
    conn, cursor = get_db_connection()
    try:
        cursor.execute("INSERT INTO RECIPES (title, story, category, photo, date_added, servings, prep_time, cook_time, user_id) VALUES (?,?,?,?,?,?,?,?,?)",(
            data['title'],
            data['story'],
            data['category'],
            data['photo'],
            data['date_added'],
            data['servings'],
            data['prep_time'],
            data['cook_time'],
            data['user_id']
        ))
    except Exception as e:
        return None
    conn.commit()
    conn.close()
    return data

def update_recipe(data, recipe_id):
    conn, cursor = get_db_connection()
    cursor.execute(f"UPDATE RECIPES SET title = '{data['title']}', story = '{data['story']}', photo = '{data['photo']}', date_added = '{data['date_added']}', servings = {data['servings']}, prep_time = {data['prep_time']}, cook_time = {data['cook_time']}, user_id = {data['user_id']} WHERE recipe_id = {recipe_id}")
    conn.commit()
    conn.close()
    return data

def remove_recipe(recipe_id):
    conn, cursor = get_db_connection(True)
    deleted_recipe = cursor.execute(f"SELECT * FROM RECIPES WHERE recipe_id = {recipe_id}").fetchone()
    cursor.execute(f"DELETE FROM RECIPES WHERE recipe_id = {recipe_id}")
    conn.commit()
    conn.close()
    return deleted_recipe

def create_user(data):
    conn, cursor = get_db_connection()
    cursor.execute(f"INSERT INTO USERS (username, password) VALUES (?,?)", (data['username'], data['password']))
    conn.commit()
    conn.close()
    return data

def fetch_users():
    conn, cursor = get_db_connection(True)
    users = cursor.execute("SELECT * FROM USERS").fetchall()
    conn.close()
    return users

def fetch_user(user_id):
    conn, cursor = get_db_connection(True)
    user = cursor.execute(f"SELECT * FROM USERS WHERE user_id = {user_id}").fetchone()
    conn.close()
    return user

def update_user(data, user_id):
    conn, cursor = get_db_connection()
    cursor.execute(f"UPDATE USERS SET username = '{data['username']}, password = '{data['password']}' WHERE user_id = {user_id}")
    conn.commit()
    conn.close()
    return data

def remove_user(user_id):
    conn, cursor = get_db_connection(True)
    deleted_user = cursor.execute(f"SELECT * FROM USERS WHERE user_id = {user_id}").fetchone()
    cursor.execute(f"DELETE FROM USERS WHERE user_id = {user_id}")
    conn.commit()
    conn.close()
    return deleted_user

def create_recipe_form(data,image ,user_id):
    ingredients = []
    directions = []
    for item in data:
        if "ingredient" in item:
            ingredients.append(data[item])
        if "direction" in item:
            directions.append(data[item])

    date_added = datetime.today().strftime('%Y-%m-%d')
    conn, cursor = get_db_connection()
    
    try:
        cursor.execute('BEGIN')

        cursor.execute('INSERT INTO RECIPES (title,story,category,photo,date_added,servings,prep_time,cook_time,user_id) VALUES (?,?,?,?,?,?,?,?,?)', (
            data['title'],
            data['story'],
            data['category'],
            image,
            date_added,
            data['servings'],
            data['prep_time'],
            data['cook_time'],
            user_id
        ))

        new_recipe_id = cursor.lastrowid

        
        for ingredient in ingredients:
            cursor.execute('INSERT INTO INGREDIENTS (ingredient, recipe_id) VALUES (?,?)', (ingredient,new_recipe_id))

        for index, direction in enumerate(directions):
            cursor.execute('INSERT INTO DIRECTIONS (step_num,step_description,recipe_id) VALUES (?,?,?)', (index,direction,new_recipe_id))

        conn.commit()
        return True
    except sqlite3.Error as e:
        conn.rollback()
        print("An error occured: ",e)
        return False
    finally:
        conn.close()

def get_ingredients(recipe_id):
    conn, cursor = get_db_connection(True)
    ingredients = cursor.execute(f"SELECT ingredient FROM INGREDIENTS WHERE recipe_id = {recipe_id}").fetchall()
    conn.close()
    return ingredients

def get_directions(recipe_id):
    conn, cursor = get_db_connection(True)
    directions = cursor.execute(f"SELECT step_description FROM DIRECTIONS WHERE recipe_id = {recipe_id}").fetchall()
    conn.close()
    return directions
