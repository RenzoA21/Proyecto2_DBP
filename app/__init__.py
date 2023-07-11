from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from .models import db, setup_db, Usuario, Receta
from utilities.utils import allowed_file
from flask import Blueprint
import os
import sys


users_bp = Blueprint('/usuarios', __name__)


def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
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
    @app.route('/recetas', methods=['POST'])
    def create_receta():
        error_code = 201
        list_errors = []
        try:
            body = request.json

            if 'medicamento' not in body:
                list_errors.append('medicamento is required')
            else:
                medicamento = body.get('medicamento')

            if 'tipo_de_toma' not in body:
                list_errors.append('tipo_de_toma is required')
            else:
                tipo_de_toma = body.get('tipo_de_toma')

            if 'cantidad' not in body:
                list_errors.append('cantidad is required')
            else:
                cantidad = body.get('cantidad')

            if 'unidad_medida' not in body:
                list_errors.append('unidad_medida is required')
            else:
                unidad_medida = body.get('unidad_medida')

            if 'porcentaje' not in body:
                list_errors.append('porcentaje is required')
            else:
                porcentaje = body.get('porcentaje')

            if 'ml_g' not in body:
                list_errors.append('ml_g is required')
            else:
                ml_g = body.get('ml_g')

            if len(list_errors) > 0:
                error_code = 400
            else:
                receta = Receta(medicamento=medicamento, tipo_de_toma=tipo_de_toma, cantidad=cantidad,
                                unidad_medida=unidad_medida, porcentaje=porcentaje, ml_g=ml_g)
                db.session.add(receta)
                db.session.commit()
                receta_id_created = receta.id

        except Exception as e:
            db.session.rollback()
            print("error: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            error_code = 500

        if error_code == 400:
            return jsonify({'success': False,
                            'message': 'Error creating Receta',
                            'errors': list_errors}), error_code
        else:
            return jsonify({'success': True,
                            'id': str(receta_id_created),
                            'message': 'Receta created successfully'
                            }), 201

    @app.route('/recetas', methods=['GET'])
    def get_recetas():
        error_code = 200
        try:
            recetas = Receta.query.all()

        except Exception as e:
            print("error: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            db.session.rollback()
            error_code = 500

        else:
            return jsonify({'success': True,
                            'recetas': [e.serialize() for e in recetas],
                            'total': len(recetas)
                            }), 200

    @users_bp.route('/usuarios', methods=['POST'])
    def create_user():
        error_lists = []
        returned_code = 201
        try:
            body = request.get_json()

            if 'nombre' not in body:
                error_lists.append('nombre is required')
            else:
                nombre = body.get('nombre')

            if 'password_hash' not in body:
                error_lists.append('password_hash is required')
            else:
                password_hash = body.get('password_hash')

            if 'email' not in body:
                error_lists.append('email is required')
            else:
                email = body.get('email')

            user_db = Usuario.query.filter_by(nombre=nombre).first()

            if user_db is not None:
                if user_db.nombre == nombre:
                    error_lists.append(
                        'An account with this username already exists')
            else:
                if len(password_hash) < 8:
                    error_lists.append(
                        'Password must have at least 8 characters')

            if len(error_lists) > 0:
                returned_code = 400
            else:
                user = Usuario(
                    nombre=nombre, password_hash=password_hash, email=email)
                user.insert()
                user_created_id = user.id

                token = jwt.encode(
                    {
                        'user_created_id': user_created_id,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                    },
                    config['SECRET_KEY'],
                    config['ALGORITHM']
                )

        except Exception as e:
            print('e:', e)
            returned_code = 500

        if returned_code == 400:
            return jsonify({
                'success': False,
                'errors': error_lists,
                'message': 'Error creating a new user'
            }), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({
                'success': True,
                'token': token,
                'user_created_id': user_created_id
            }), returned_code

    @users_bp.route('/api/signin', methods=['POST'])
    def login():
        pass

    @users_bp.route('/usuarios/<usuario_id>', methods=['DELETE'])
    def delete_user(usuario_id):
        returned_code = 200

        try:
            user = Usuario.query.get(usuario_id)
            if user is None:
                returned_code = 404

            user.delete()
        except Exception as e:
            print('e:', e)
            returned_code = 500

        if returned_code != 200:
            abort(returned_code)
        else:
            return jsonify({
                'success': True
            }), returned_code

    return app
