import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db_connection(AsDict = False):
    conn = sqlite3.connect('recipes.db')   
    conn.execute("PRAGMA foreign_keys = ON")
    if AsDict:
        conn.row_factory = dict_factory
    cursor = conn.cursor()
    return conn, cursor