from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from .models import db, setup_db, Usuario, Receta, Cajero, Delivery
from utilities.utils import allowed_file
from flask import Blueprint
import os
import sys
from datetime import datetime


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

    @app.route('/cajeros', methods=['POST'])
    def create_cajero():
        error_code = 201
        list_errors = []
        try:
            body = request.json

            if 'registro_inscripcion' not in body:
                list_errors.append('registro_inscripcion is required')
            else:
                registro_inscripcion = body.get('registro_inscripcion')

            if 'verificacion' not in body:
                list_errors.append('verificacion is required')
            else:
                verificacion = body.get('verificacion')

            if 'necesidad' not in body:
                list_errors.append('necesidad is required')
            else:
                necesidad = body.get('necesidad')

            if 'validacion' not in body:
                list_errors.append('validacion is required')
            else:
                validacion = body.get('validacion')

            if 'costo' not in body:
                list_errors.append('costo is required')
            else:
                costo = body.get('costo')

            if 'entrega' not in body:
                list_errors.append('entrega is required')
            else:
                entrega = body.get('entrega')

            if len(list_errors) > 0:
                error_code = 400
            else:
                cajero = Cajero(
                    registro_inscripcion=registro_inscripcion,
                    verificacion=verificacion,
                    necesidad=necesidad,
                    validacion=validacion,
                    costo=costo,
                    entrega=entrega
                )
                db.session.add(cajero)
                db.session.commit()
                cajero_id_created = cajero.id

        except Exception as e:
            db.session.rollback()
            print("error: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            error_code = 500

        if error_code == 400:
            return jsonify({
                'success': False,
                'message': 'Error creating Cajero',
                'errors': list_errors
            }), error_code
        else:
            return jsonify({
                'success': True,
                'id': str(cajero_id_created),
                'message': 'Cajero created successfully'
            }), 201

    @app.route('/cajeros', methods=['GET'])
    def get_cajeros():
        error_code = 200
        try:
            cajeros = Cajero.query.all()
        except Exception as e:
            print("error: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            db.session.rollback()
            error_code = 500

        return jsonify({
            'success': True,
            'cajeros': [cajero.serialize() for cajero in cajeros],
            'total': len(cajeros)
        }), error_code

    @app.route('/deliveries', methods=['POST'])
    def create_delivery():
        error_code = 201
        list_errors = []
        try:
            body = request.json

            if 'direccion' not in body:
                list_errors.append('direccion is required')
            else:
                direccion = body.get('direccion')

            if 'vehiculo' not in body:
                list_errors.append('vehiculo is required')
            else:
                vehiculo = body.get('vehiculo')

            if 'placa' not in body:
                list_errors.append('placa is required')
            else:
                placa = body.get('placa')

            if 'metodo_pago' not in body:
                list_errors.append('metodo_pago is required')
            else:
                metodo_pago = body.get('metodo_pago')

            hora_entrega = datetime.now()

            if 'image_pedido' in body:
                image_pedido = body.get('image_pedido')
            else:
                image_pedido = None

            if len(list_errors) > 0:
                error_code = 400
            else:
                delivery = Delivery(
                    direccion=direccion,
                    vehiculo=vehiculo,
                    placa=placa,
                    metodo_pago=metodo_pago,
                    hora_entrega=hora_entrega,
                    image_pedido=image_pedido
                )
                db.session.add(delivery)
                db.session.commit()
                delivery_id_created = delivery.id

        except Exception as e:
            db.session.rollback()
            print("error: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            error_code = 500

        if error_code == 400:
            return jsonify({'success': False,
                            'message': 'Error creating Delivery',
                            'errors': list_errors}), error_code
        else:
            return jsonify({'success': True,
                            'id': str(delivery_id_created),
                            'message': 'Delivery created successfully'
                            }), 201

    @app.route('/deliveries', methods=['GET'])
    def get_deliveries():
        error_code = 200
        try:
            deliveries = Delivery.query.all()
        except Exception as e:
            print("error: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            db.session.rollback()
            error_code = 500

        else:
            return jsonify({'success': True,
                            'deliveries': [delivery.serialize() for delivery in deliveries],
                            'total': len(deliveries)
                            }), 200

    @app.route("/sessiones", methods=["POST"])
    def login():

        username = request.json.get("username", None)
        password = request.json.get("password", None)

        # Aquí deberías verificar las credenciales con tu base de datos
        if username != "test" or password != "test":
            return jsonify({"msg": "Credenciales incorrectas"}), 401

        return jsonify({"msg": "credenciales correctas"}), 401

    @users_bp.route('/api/signin', methods=['POST'])
    def login():
        pass

    return app
