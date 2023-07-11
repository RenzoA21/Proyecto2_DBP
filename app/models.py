from datetime import datetime
import uuid
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sys

config = {
    'DATABASE_URI': 'postgresql://postgres:1234@localhost:5432/christian',
}

database_uri = config['DATABASE_URI']

db = SQLAlchemy()


def setup_db(app, database_path=database_uri):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(
        uuid.uuid4()), server_default=db.text('uuid_generate_v4()'))
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    apellido = db.Column(db.String(50), unique=True, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(400), nullable=False)
    sexo = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    def __init__(self, nombre, apellido, password_hash, sexo, fecha_nacimiento, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.password_hash = password_hash
        self.sexo = sexo if sexo in ['Masculino', 'Femenino'] else None
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'password_hash': self.password_hash,
            'sexo': self.sexo,
            'fecha_nacimiento': self.fecha_nacimiento.isoformat(),
            'telefono': self.telefono,
            'email': self.email
        }

    @property
    def password(self):
        raise AttributeError('Passwor is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User{self.id} - {self.nombre}-{self.apellido}>'

        def insert(self):
            try:
                db.session.add(self)
                db.session.commit()
                user_created_id = self.id
            except Exception as e:
                print(sys.exc_info())
                print('e: ', e)
                db.session.rollback()
            finally:
                db.session.close()

            return user_created_id

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print(sys.exc_info())
            print('e: ', e)
            db.session.rollback()


class Receta(db.Model):
    __tablename__ = 'receta'

    id = db.Column(db.Integer, primary_key=True)
    medicamento = db.Column(db.String(100), nullable=False)
    tipo_de_toma = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    unidad_medida = db.Column(db.String(50), nullable=False)
    porcentaje = db.Column(db.Float, nullable=False)
    ml_g = db.Column(db.Float, nullable=False)

    def __init__(self, medicamento, tipo_de_toma, cantidad, unidad_medida, porcentaje, ml_g):
        self.medicamento = medicamento
        self.tipo_de_toma = tipo_de_toma
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida
        self.porcentaje = porcentaje
        self.ml_g = ml_g

    def serialize(self):
        return {
            'id': self.id,
            'medicamento': self.medicamento,
            'tipo_de_toma': self.tipo_de_toma,
            'cantidad': self.cantidad,
            'unidad_medida': self.unidad_medida,
            'porcentaje': self.porcentaje,
            'ml_g': self.ml_g
        }


class Cajero(db.Model):
    __tablename__ = 'cajero'

    id = db.Column(db.Integer, primary_key=True)
    registro_inscripcion = db.Column(db.String(100), nullable=False)
    verificacion = db.Column(db.Boolean, default=True,
                             nullable=False)  # Verificacion (Si, No)
    necesidad = db.Column(db.String(200), nullable=False)
    validacion = db.Column(db.Boolean, default=True,
                           nullable=False)  # Validacion (Si, No)
    costo = db.Column(db.Float, nullable=False)
    entrega = db.Column(db.Boolean, default=True,
                        nullable=False)  # Entrega (Si, No)

    def __init__(self, registro_inscripcion, verificacion, necesidad, validacion, costo, entrega):
        self.registro_inscripcion = registro_inscripcion
        self.verificacion = verificacion
        self.necesidad = necesidad
        self.validacion = validacion
        self.costo = costo
        self.entrega = entrega

    def serialize(self):
        return {
            'id': self.id,
            'registro_inscripcion': self.registro_inscripcion,
            'verificacion': self.verificacion,
            'necesidad': self.necesidad,
            'validacion': self.validacion,
            'costo': self.costo,
            'entrega': self.entrega
        }


class Delivery(db.Model):
    __tablename__ = 'delivery'

    id = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(200), nullable=False)
    vehiculo = db.Column(db.String(100), nullable=False)
    placa = db.Column(db.String(20), nullable=False)
    metodo_pago = db.Column(db.String(50), nullable=False)
    hora_entrega = db.Column(db.DateTime(timezone=True), nullable=True, onupdate=datetime.utcnow,
                             server_default=db.text('now()'))
    image_pedido = db.Column(db.String(500), nullable=True)

    def __init__(self, direccion, vehiculo, placa, metodo_pago, hora_entrega, image_pedido=None):
        self.direccion = direccion
        self.vehiculo = vehiculo
        self.placa = placa
        self.metodo_pago = metodo_pago
        self.hora_entrega = hora_entrega
        self.image_pedido = image_pedido

    def serialize(self):
        return {
            'id': self.id,
            'direccion': self.direccion,
            'vehiculo': self.vehiculo,
            'placa': self.placa,
            'metodo_pago': self.metodo_pago,
            'hora_entrega': str(self.hora_entrega),
            'image_pedido': self.image_pedido
        }
