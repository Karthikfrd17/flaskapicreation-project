import unittest
import requests
from app.config.config import API_SECRET_TOKEN
import logging



class APITestCase(unittest.TestCase):
    def setUp(self):
        from app.run import app
        app.testing = True
        self.app = app.test_client()
        self.headers = {'Authorization': API_SECRET_TOKEN}
    
    def test_valid_input(self):
        sentence = "This is a valid sentence."
        payload = {'sentence': sentence}
        response = self.app.post('/random_array', json=payload, headers=self.headers)
        data = response.get_json() 
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['sentence'], sentence)
        self.assertIsInstance(data['random_array'], list)
        self.assertEqual(len(data['random_array']), 500)
    
    def test_missing_sentence_parameter(self):
        payload = {}
        response = self.app.post('/random_array', json=payload, headers=self.headers)
        data = response.get_json()
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Invalid input. Sentence cannot be empty.')

    def test_authentication_failure(self):
        sentence = "This is a valid sentence."
        payload = {'sentence': sentence}
        headers = {'Authorization': 'invalid_token'}
        response = self.app.post('/random_array', json=payload, headers='headers')
        data = response.get_json()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Authentication failed.')

    def test_authentication_failure_missing_token(self):
        sentence = "This is a valid sentence."
        payload = {'sentence': sentence}
        headers = {}  # Missing Authorization header
        response = self.app.post('/random_array', json=payload, headers=headers)
        data = response.get_json()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Authentication failed.')
        logging.error(f'Authentication failed for sentence: {sentence}')


if __name__ == '__main__':
    unittest.main()
