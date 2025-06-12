from flask import Blueprint, request, jsonify, render_template, redirect, url_for
import sqlite3
from app.models.OLD_usuario_model import *

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuarios_bp.route("/nuevo", methods=['POST'])
def registrar_usuario():
    
    print("Intentado crear un usuario")
    
    #Para HTML
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    
    # data = request.get_json()  #Cargar los datos para la API
    # nombre = data.get('nombre')
    # email = data.get('email')
    
    if not nombre or not email:
        #return jsonify({"error":"Faltan datos"}), 400 #respuesta por API
        return render_template("usuarios/agregar_usuario.html", error="Faltan datos") #Respuesta HTML
    try:
        usuario_id = crear_usuario(nombre,email)
        print("Usuario creado con exito")
        return redirect(url_for("usuarios.obtener_usuarios"))
        
    except Exception as e:
        return render_template("usuarios/agregar_usuario.html", error=str(e))
        #return jsonify({"id":usuario_id, "nombre":nombre, "email":email}), 201 #Respuesta API

@usuarios_bp.route("/nuevo", methods=['GET'])
def mostrar_formulario_usuario():
    return render_template("usuarios/agregar_usuario.html")


@usuarios_bp.route("/", methods = ['GET'])

def obtener_usuarios():
    try:
        q = request.args.get('q', '')  # Toma el parámetro de búsqueda

        usuarios = mostrar_usuarios()  # Trae todos
        if q:
            usuarios = [u for u in usuarios if q.lower() in u[1].lower()]  # Filtra por nombre

        return render_template("usuarios/lista_usuarios.html", usuarios=usuarios)

    except Exception as e:
        return render_template("usuarios/lista_usuarios.html", usuarios=[], error=str(e))
# def obtener_usuarios():
    
#     try:
#         usuarios = mostrar_usuarios()
#         lista_usuarios = [{"id":u[0], "nombre": u[1], "email": u[2]} for u in usuarios]
        
#         #return jsonify(lista_usuarios), 201 #Respuesta a la API
#         return render_template("usuarios/lista_usuarios.html", usuarios = usuarios) #Respuesta visual html
    
#     except Exception as e:
#         return jsonify({"error": str(e)})
    
    

@usuarios_bp.route("/<int:id>", methods = ['GET'])
def obtener_usuarios_por_id(id):
    
    try:
        usuario = mostrar_usuario_por_id(id)
        if usuario is None:
            return jsonify({"Error": "El usuario no existe"})
        
        mostrar_usuario = [{"id":usuario[0], "nombre": usuario[1], "email": usuario[2]}]
        return jsonify(mostrar_usuario), 201

    except Exception as e:
        return jsonify({"error": str(e)})
    
@usuarios_bp.route("/<int:id>", methods = ['DELETE'])
def eliminar_usuarios_id(id):
    
    try:
        usuario = eliminar_usuario_por_id(id)
        
        if usuario == 0:
            return jsonify({"Error": "El usuario no existe"}), 404
        
        return jsonify({"Success": "Usuario eliminado con exito"}), 200

    except Exception as e:
        return jsonify({"error": str(e)})
    
@usuarios_bp.route("/<int:id>", methods = ['PUT'])
def editar_usuarios_id(id):
    
    print("Intentado modificar un usuario")
    
    try: 
        data = request.get_json()
        nombre = data.get('nombre')
        email = data.get('email')
        
        actualizado = editar_usuario_por_id(id, nombre, email)
    
        if not actualizado:
            return jsonify({"Error": "No se encontró el usuario o no se enviaron datos."})
        
        return jsonify(
            {"id":id,
             "nombre":nombre,
             "email":email,
             "mensaje":"Usuario actualizado con exito"}), 200

    except Exception as e:
        return jsonify({"error": str(e)})