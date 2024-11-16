from ..utils import get_db_connection

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

def fetch_user_by_username(username):
    conn, cursor = get_db_connection(True)
    user = cursor.execute(f"SELECT * FROM USERS WHERE username = '{username}'").fetchone()
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

def check_user_exists(username):
    conn, cursor = get_db_connection(True)
    user = cursor.execute(f"SELECT * FROM USERS WHERE username = '{username}'").fetchone()
    conn.close()

    if user:
        return True
    else:
        return False