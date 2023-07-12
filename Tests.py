import json
import unittest
from datetime import datetime
from app.models import Usuario, Receta, Cajero, Delivery
from app import create_app
config = {
    'DATABASE_URI': 'postgresql://postgres:1234@localhost:5432/christian',
}


class Tests(unittest.TestCase):
    def setUp(self):
        database_qa = config['DATABASE_URI']
        self.app = create_app({'database_qa': database_qa})
        self.client = self.app.test_client()

    def test_create_receta(self):
        response = self.client.post('/recetas', json={
            'medicamento': 'Ibuprofeno',
            'tipo_de_toma': 'Oral',
            'cantidad': 1,
            'unidad_medida': 'tableta',
            'porcentaje': 5.0,
            'ml_g': 500.0
        })
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['id'])
        self.assertEqual(data['message'], 'Receta created successfully')

    def test_create_receta_missing_fields(self):
        response = self.client.post('/recetas', json={'medicamento': 'Ibuprofeno',
                                                      'tipo_de_toma': 'Oral',
                                                      'cantidad': 1,
                                                      'unidad_medida': 'tableta',
                                                      'porcentaje': 5.0})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Error creating Receta')
        self.assertIn('ml_g is required', data['errors'])

    def test_get_recetas(self):
        response = self.client.get('/recetas')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['recetas'])
        self.assertEqual(data['total'], len(data['recetas']))

    def test_create_cajero(self):
        response = self.client.post('/cajeros', json={
            'registro_inscripcion': '12345',
            'verificacion': True,
            'necesidad': 'Pago de servicios',
            'validacion': False,
            'costo': 10.5,
            'entrega': True
        })
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['id'])
        self.assertEqual(data['message'], 'Cajero created successfully')

    def test_cajero_receta_missing_fields(self):
        response = self.client.post('/cajeros', json={'registro_inscripcion': '12345',
                                                      'verificacion': True,
                                                      'necesidad': 'Pago de servicios',
                                                      'validacion': False,
                                                      'costo': 10.5
                                                      })
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Error creating Cajero')
        self.assertIn('entrega is required', data['errors'])

    def test_get_cajeros(self):
        response = self.client.get('/cajeros')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['cajeros'])
        self.assertIsInstance(data['cajeros'], list)

    def test_create_delivery(self):
        response = self.client.post('/deliveries', json={
            'direccion': 'Calle Principal 123',
            'vehiculo': 'Auto',
            'placa': 'ABC123',
            'metodo_pago': 'Tarjeta'
        })
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['id'])
        self.assertEqual(data['message'], 'Delivery created successfully')

    def test_delivery_receta_missing_fields(self):
        response = self.client.post('/deliveries', json={'direccion': 'Calle Principal 123',
                                                         'vehiculo': 'Auto',
                                                         'placa': 'ABC123',
                                                         })
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Error creating Delivery')
        self.assertIn('metodo_pago is required', data['errors'])

    def test_get_deliveries(self):
        response = self.client.get('/deliveries')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['deliveries'], list)
        self.assertEqual(data['total'], len(data['deliveries']))

    def test_login_success(self):
        response = self.client.post("/sessiones", json={
            "username": "test",
            "password": "test"
        })
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"msg": "credenciales correctas"})

    def test_login_failure(self):
        response = self.client.post("/sessiones", json={
            "username": "wrong",
            "password": "wrong"
        })
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"msg": "Credenciales incorrectas"})
