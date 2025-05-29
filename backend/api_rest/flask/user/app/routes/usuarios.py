from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.models.usuario_model import *
from sqlalchemy.exc import SQLAlchemyError

#Blueprint, todo lo que tenga prefijo usuarios_bp la ruta va a ser /usuarios
usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')



@usuarios_bp.route("/nuevo", methods = ['GET'])
def mostrar_formulario_usuario():
    return render_template("usuarios/agregar_usuario.html")

#Lo trabajo híbrido, como form get y como json
@usuarios_bp.route("/nuevo", methods = ['POST'])
def crear_usuario():
    
    if request.is_json():
        data = request.get_json()
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        email = data.get('email')
        password = data.get('password')
    else:
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        password = request.form.get('password')
    
    if not nombre or not email or not password:
        error_msg = "Faltan nombre, email o contraseña"
        
        #Acepta tipo json o HTML, si es json da error 400, si es html renderiza
        if request.accept_mimetypes.accept_json:
            return jsonify({'error': error_msg}), 400
        else:
            return render_template("usuarios/agregar_usuario.html", error=error_msg)
        
    
    try:
        nuevo_usuario = Usuario(nombre=nombre,apellido=apellido,email=email)
        nuevo_usuario.set_password(password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        
        if request.accept_mimetypes.accept_json:
            return jsonify({
                'mensaje': 'Usuario creado con éxito',
                'usuario': {
                    'id': nuevo_usuario.id,
                    'nombre': nuevo_usuario.nombre,
                    'apellido': nuevo_usuario.apellido,
                    'email': nuevo_usuario.email
                }
            }), 201
        else:
            return redirect(url_for('usuarios.obtener_usuarios'))
    
    except SQLAlchemyError as e:
        db.session.rollback()
        error_msg = str(e)
        
        if request.accept_mimetypes.accept_json:
            return jsonify({'error': error_msg}), 500
        else:
            return render_template("usuarios/agregar_usuario.html", error=str(e))
    
@usuarios_bp.route("/", methods = ['GET'])
def obtener_usuarios():
    try:
        q = request.args.get('q', '')
        usuarios = Usuario.query.all() 

        if q:
            usuarios = [u for u in usuarios if q.lower() in u.nombre.lower()]

        if request.accept_mimetypes.accept_json:
            usuarios_json = [{
                'id': u.id,
                'nombre': u.nombre,
                'apellido': u.apellido,
                'email': u.email
            } for u in usuarios]
            
            return jsonify(usuarios_json),200
        
        return render_template("usuarios/lista_usuarios.html", usuarios = usuarios)

    except SQLAlchemyError as e:
        error_msg = str(e)
        
        if request.accept_mimetypes.accept_json:
            return jsonify({'error': error_msg}), 500
        else:
            return render_template("usuarios/lista_usuarios.html", error = error_msg)
    

@usuarios_bp.route("/eliminar/<int:pk>", methods = ['POST'])
def eliminar_usuario(pk):
    
    try:
        usuario = Usuario.query.get_or_404(pk)
        db.session.delete(usuario)
        db.session.commit()
        
        if request.accept_mimetypes.accept_json:
            return jsonify({'Mensaje':'Usuario eliminado con éxito'}),201
        else:      
            return redirect(url_for('usuarios.obtener_usuarios'))
    
    except SQLAlchemyError as e:
        db.session.rollback()
        error_msg = str(e)
        
        if request.accept_mimetypes.accept_json:
            return jsonify({"error":error_msg}), 500
        else:
            return render_template("usuarios/lista_usuarios.html", error = error_msg)
    
@usuarios_bp.route("/editar/<int:pk>", methods=['GET'])
def mostrar_formulario_editar(pk):
    usuario = Usuario.query.get_or_404(pk)
    return render_template("usuarios/editar_usuario.html", usuario=usuario)

@usuarios_bp.route("/editar/<int:pk>", methods=['POST'])
def editar_usuario(pk):
    usuario = Usuario.query.get_or_404(pk)

    if request.is_json():
        data = request.get_json()
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        email = data.get('email')
        password = data.get('password')
    else:
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        password = request.form.get('password')

    if not nombre or not email:
        error_msg = "Nombre y email son obligatorios"
        
        if request.accept_mimetypes.accept_json:
            return jsonify({'Error': error_msg}), 400
        else:
            return render_template("usuarios/editar_usuario.html", usuario=usuario, error=error_msg)
    
    try:
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.email = email

        if password:
            usuario.set_password(password)  # solo actualiza si se puso nueva contraseña

        db.session.commit()
        return redirect(url_for('usuarios.obtener_usuarios'))

    except SQLAlchemyError as e:
        db.session.rollback()
        error_msg = str(e)
        
        if request.accept_mimetypes.accept_json:
            return jsonify({"Error":error_msg}),500
        else:
            return render_template("usuarios/editar_usuario.html", usuario=usuario, error=error_msg)