import base64
from datetime import datetime
import sqlite3
from ..utils import get_db_connection

def create_review(recipe_id,user_id ,data ):
    try:
        conn, cursor = get_db_connection(True)
        cursor.execute("INSERT INTO REVIEWS (rating, review, review_date, user_id, recipe_id) VALUES (?,?,?,?,?)",(
            data['rating'],
            data['review'],
            datetime.today().strftime('%Y-%m-%d'),
            user_id,
            recipe_id
        ))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print("An error occured:",e)
        return False
    finally:
        conn.close()

def fetch_reviews(recipe_id):
    try:
        conn, cursor = get_db_connection(True)
        reviews = cursor.execute(f'SELECT * FROM REVIEWS LEFT JOIN USERS ON REVIEWS.user_id = USERS.user_id WHERE recipe_id = {recipe_id}').fetchall()
        print("fetch successful")
        print(reviews)
        return reviews
    except:
        return {"error" : "an error occured"}
    finally:
        conn.close()