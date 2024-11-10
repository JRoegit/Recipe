import sqlite3

def initdb():
    conn = sqlite3.connect('recipes.db')
    with open('schema.sql', 'r') as sql_file:
        conn.executescript(sql_file.read())
    conn.close()
    print("DB initialized.")

if __name__ == "__main__":
    initdb()