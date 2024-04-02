"""
Module Documentation: api.py

This module implements a Flask application to handle API routes for accessing Tigrinya characters, their variations, English representations, and audio pronunciations.

Routes:
1. /api/characters: Retrieves all Tigrinya characters and their English representations.
2. /api/character_variations: Retrieves all variations of all Tigrinya characters.
3. /api/character_variations/<character>: Retrieves all variations of a specific Tigriny character.
4. /api/character/<character>: Retrieves the English representation of a specific Tigrinya character.
5. /api/character/<character>/pronunciation: Retrieves the audio pronunciation of a specific Tigrinya character.

Functions:
- get_characters: Handles the route to retrieve all Tigrinya characters and their English representations.
- get_character_variations: Handles the route to retrieve all variations of all Tigrinya characters.
- get_character_variations_by_character: Handles the route to retrieve all variations of a specific Tigrinya character.
- get_character_info: Handles the route to retrieve the English representation of a specific Tigrinya character.
- get_character_pronunciation: Handles the route to retrieve the audio pronunciation of a specific Tigrinya character.

Usage:
- Import this module to start the Flask application for handling API requests related to Tigrinya characters.
- Run the module to start the Flask server and make the API endpoints accessible for client requests.
"""
from flask import Flask, jsonify, request, send_file, send_from_directory, url_for
import api_methods

app = Flask(__name__)


# Route to get all characters
@app.route('/api/characters', methods=['GET'])
def get_characters():
    """
    Retrieves all Tigrinya characters and their English representations.
    
    Returns:
        JSON: A JSON object containing all Tigrinya characters and their English representations.
    """
    characters = api_methods.TIGRINYA_CHARACTERS
    english_representations = api_methods.ENG_REPRESENTATION
    character_data = [{'character': char, 'english_representation': eng} for char, eng in zip(characters, english_representations)]
    return jsonify(character_data)


# Route to get all characters variations
@app.route('/api/character_variations', methods=['GET'])
def get_character_variations():
    """
    Retrieves all variations of all Tigrinya characters.
    
    Returns:
        JSON: A JSON object containing all variations of Tigrinya characters.
    """
    character_variations = api_methods.get_character_variations()
    return jsonify(character_variations)


# Route to get a specific character's variations
@app.route('/api/character_variations/<character>', methods=['GET'])
def get_character_variations_by_character(character):
    """
    Retrieves all variations of a specific Tigrinya characters.
    
    Returns:
        JSON: A JSON object containing all variations of a specific Tigrinya characters.
    """
    character_variations = api_methods.get_variations(character)
    if character_variations:
        return jsonify({character: character_variations})
    else:
        return jsonify({'error': 'Character not found'}), 404


# Route to get a specific character and its English representation
@app.route('/api/character/<character>', methods=['GET'])
def get_character_info(character):
    """
    Retrieves the English representation of a specific Tigrinya character.
    
    Args:
        character (str): The Tigrinya character.
        
    Returns:
        JSON: A JSON object containing the Tigrinya character and its English representation.
    """
    english_representation = api_methods.get_english_representation(character)
    if english_representation:
        return jsonify({'character': character, 'english_representation': english_representation})
    else:
        return jsonify({'error': 'Character not found'}), 404


# Route to get a specific character and its audio pronunciation
@app.route('/api/character/<character>/pronunciation', methods=['GET'])
def get_character_pronunciation(character):
    """
    Retrieves the audio pronunciation of a specific Tigrinya character.
    
    Args:
        character (str): The Tigrinya character.
        
    Returns:
        JSON: A Tigrinya characters audio pronunciation file.
    """
    audio_file_path = api_methods.get_audio_pronunciation(character)
    if audio_file_path:
        return send_file(audio_file_path, mimetype='audio/wav')
    else:
        return jsonify({'error': 'Character not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
