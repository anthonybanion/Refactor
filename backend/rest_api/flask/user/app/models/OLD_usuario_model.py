import sqlite3

DB_PATH = "db_api.sqlite"

def crear_usuario(nombre,email):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email) values (?,?)",(nombre,email))
        conn.commit()
    

def mostrar_usuarios():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
    return usuarios

def mostrar_usuario_por_id(id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
        usuario = cursor.fetchone()
    return usuario

def eliminar_usuario_por_id(id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        conn.commit()
    return cursor.rowcount

def editar_usuario_por_id(id, nombre, email):
    
    campos = []
    valores = []
    
    if nombre:
        campos.append("nombre = ?")
        valores.append(nombre)
    
    if email:
        campos.append("email = ?")
        valores.append(email)
        
    if not campos:
        return False
    valores.append(id)
    
    query = f"UPDATE usuarios SET {', '.join(campos)} WHERE id = ?"
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(query,valores)
        conn.commit()
        return cursor.rowcount > 0