from flask import (
    Flask,
    request,
    jsonify
)

from .models import db, setup_db, Usuario, Receta, Cajero, Delivery
from flask_cors import CORS
from utilities.utils import allowed_file

import os
import sys


app = Flask(__name__)
setup_db(app)

# Definir los endpoints para cada clase


@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.serialize() for usuario in usuarios])


@app.route('/api/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(**data)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify(nuevo_usuario.serialize()), 201


@app.route('/api/usuarios/<int:usuario_id>', methods=['PATCH'])
def update_usuario(usuario_id):
    data = request.get_json()
    usuario = Usuario.query.get(usuario_id)
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    for key, value in data.items():
        setattr(usuario, key, value)
    db.session.commit()
    return jsonify(usuario.serialize())


@app.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'success': True})
