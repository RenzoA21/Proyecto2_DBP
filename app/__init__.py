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

    @app.route('/api/recetas', methods=['GET'])
    def get_recetas():
        recetas = Receta.query.all()
        return jsonify([receta.serialize() for receta in recetas])


    @app.route('/api/recetas', methods=['POST'])
    def create_receta():
        data = request.get_json()
        nueva_receta = Receta(**data)
        db.session.add(nueva_receta)
        db.session.commit()
        return jsonify(nueva_receta.serialize()), 201


    @app.route('/api/recetas/<int:receta_id>', methods=['PATCH'])
    def update_receta(receta_id):
        data = request.get_json()
        receta = Receta.query.get(receta_id)
        if receta is None:
            return jsonify({'error': 'Receta no encontrada'}), 404
        for key, value in data.items():
            setattr(receta, key, value)
        db.session.commit()
        return jsonify(receta.serialize())


    @app.route('/api/recetas/<int:receta_id>', methods=['DELETE'])
    def delete_receta(receta_id):
        receta = Receta.query.get(receta_id)
        if receta is None:
            return jsonify({'error': 'Receta no encontrada'}), 404
    db.session.delete(receta)
    db.session.commit()
    return jsonify({'success': True})


    @app.route('/api/cajeros', methods=['GET'])
    def get_cajeros():
        cajeros = Cajero.query.all()
        return jsonify([cajero.serialize() for cajero in cajeros])


    @app.route('/api/cajeros', methods=['POST'])
    def create_cajero():
        data = request.get_json()
        nuevo_cajero = Cajero(**data)
        db.session.add(nuevo_cajero)
        db.session.commit()
        return jsonify(nuevo_cajero.serialize()), 201


    @app.route('/api/cajeros/<int:cajero_id>', methods=['PATCH'])
    def update_cajero(cajero_id):
        data = request.get_json()
        cajero = Cajero.query.get(cajero_id)
        if cajero is None:
            return jsonify({'error': 'Cajero no encontrado'}), 404
        for key, value in data.items():
            setattr(cajero, key, value)
        db.session.commit()
        return jsonify(cajero.serialize())


    @app.route('/api/cajeros/<int:cajero_id>', methods=['DELETE'])
    def delete_cajero(cajero_id):
        cajero = Cajero.query.get(cajero_id)
        if cajero is None:
            return jsonify({'error': 'Cajero no encontrado'}), 404
        db.session.delete(cajero)
        db.session.commit()
        return jsonify({'success': True})


    @app.route('/api/delivery', methods=['GET'])
    def get_deliverys():
        deliverys = Delivery.query.all()
        return jsonify([delivery.serialize() for delivery in deliverys])


    @app.route('/api/delivery', methods=['POST'])
    def create_delivery():
        data = request.get_json()
        nuevo_delivery = Delivery(**data)
        db.session.add(nuevo_delivery)
        db.session.commit()
        return jsonify(nuevo_delivery.serialize()), 201


    @app.route('/api/delivery/<int:delivery_id>', methods=['PATCH'])
    def update_delivery(delivery_id):
        data = request.get_json()
        delivery = Delivery.query.get(delivery_id)
        if delivery is None:
            return jsonify({'error': 'Delivery no encontrado'}), 404
        for key, value in data.items():
            setattr(delivery, key, value)
        db.session.commit()
        return jsonify(delivery.serialize())


    @app.route('/api/delivery/<int:delivery_id>', methods=['DELETE'])
    def delete_delivery(delivery_id):
        delivery = Delivery.query.get(delivery_id)
        if delivery is None:
            return jsonify({'error': 'Delivery no encontrado'}), 404
        db.session.delete(delivery)
        db.session.commit()
        return jsonify({'success': True})

    return app
