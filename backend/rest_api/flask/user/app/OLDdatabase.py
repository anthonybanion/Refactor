import sqlite3

DB_PATH = "db_api.sqlite"

def crear_base():
    print("Creando base de datos...")
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS usuarios(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       email TEXT NOT NULL UNIQUE
                       )
                       ''')
        conn.commit()
    print("Base de datos creada con exito")