import json
import unittest
from app.models import Usuario, Receta
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

    def test_create_tienda_missing_fields(self):
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
