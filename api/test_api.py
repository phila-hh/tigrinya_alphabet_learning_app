"""
Module Documentation: test_api.py

This module contains a collection of unit tests for the API routes implemented in the Flask application. Each test case verifies the functionality and behavior of a specific API endpoint by sending HTTP requests and inspecting the responses.

Classes:
- TestAPIRoutes: A subclass of unittest.TestCase that contains individual test methods for different API routes.

Test Methods:
1. test_get_characters: Tests the /api/characters route to ensure it returns a list of Tigrinya characters and their English representations.
2. test_get_character_variations: Tests the /api/character_variations route to ensure it returns a dictionary containing variations of Tigrinya characters.
3. test_get_character_variations_specific_character: Tests the /api/character_variations/<character> route to ensure it returns a list of variations for a specific Tigrinya character.
4. test_get_character_info: Tests the /api/character/<character> route to ensure it returns the English representation of a specific Tigrinya character.
5. test_get_character_pronunciation: Tests the /api/character/<character>/pronunciation route to ensure it returns the audio pronunciation of a specific Tigrinya character in WAV format.

Usage:
- To run the tests, execute the module directly (python test_api.py) or using a test runner.

Note:
- Each test method checks the HTTP response status code and the data format/content returned by the API endpoints to ensure correctness and consistency.
- Additional checks can be added to verify specific properties of the API responses as needed.
"""

import unittest
from flask import json
from api import app


class TestAPIRoutes(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_characters(self):
        response = self.app.get('/api/characters')
        data = json.loads(response.data.decode('utf-8'))
        
        # Check if response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check if response is a list
        self.assertIsInstance(data, list)
        
        # Check if each item in the response has 'character' and 'english_representation' keys
        for item in data:
            self.assertIn('character', item)
            self.assertIn('english_representation', item)

    def test_get_character_variations(self):
        response = self.app.get('/api/character_variations')
        data = json.loads(response.data.decode('utf-8'))
        
        # Check if response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check if response is a dictionary
        self.assertIsInstance(data, dict)

    def test_get_character_variations_specific_character(self):
        response = self.app.get('/api/character_variations/ለ')
        data = json.loads(response.data.decode('utf-8'))
        
        # Check if response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check if response is a list
        self.assertIsInstance(data, dict)

    def test_get_character_info(self):
        response = self.app.get('/api/character/ለ')
        data = json.loads(response.data.decode('utf-8'))
        
        # Check if response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check if response is a dictionary
        self.assertIsInstance(data, dict)
        
        # Check if response contains 'character' and 'english_representation' keys
        self.assertIn('character', data)
        self.assertIn('english_representation', data)

    def test_get_character_pronunciation(self):
        response = self.app.get('/api/character/ለ/pronunciation')
        
        # Check if response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check if response has the correct content type
        self.assertEqual(response.content_type, 'audio/wav')

if __name__ == '__main__':
    unittest.main()
