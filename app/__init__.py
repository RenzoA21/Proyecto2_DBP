from flask import Flask, request, jsonify
from flask_cors import CORS
from .models import db, setup_db, Usuario, Receta, Cajero, Delivery
from utilities.utils import allowed_file

import os
import sys


def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        app.config['UPLOAD_FOLDER'] = 'static/employees'
        setup_db(app)
        CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add(' Access-Control-Max-Age', '10')
        return response

    # Definir los endpoints para cada clase

    @app.route('/usuarios', methods=['GET'])
    def get_usuarios():
        usuarios = Usuario.query.all()
        return jsonify([usuario.serialize() for usuario in usuarios])

    @app.route('/usuarios', methods=['POST'])
    def create_usuario():
        data = request.get_json()
        nuevo_usuario = Usuario(**data)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify(nuevo_usuario.serialize()), 201

    @app.route('/usuarios/<int:usuario_id>', methods=['PATCH'])
    def update_usuario(usuario_id):
        data = request.get_json()
        usuario = Usuario.query.get(usuario_id)
        if usuario is None:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        for key, value in data.items():
            if hasattr(usuario, key):
                setattr(usuario, key, value)
        db.session.commit()
        return jsonify(usuario.serialize())

    @app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
    def delete_usuario(usuario_id):
        usuario = Usuario.query.get(usuario_id)
        if usuario is None:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'success': True})

    return app
