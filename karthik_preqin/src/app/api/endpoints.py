from flask import Blueprint, request, jsonify
import numpy as np
import logging
from app.config.config import API_SECRET_TOKEN

api_bp = Blueprint('api', __name__)

@api_bp.route('/random_array', methods=['POST', 'GET'])  # Allow GET requests
def random_array():
    """
    API endpoint that takes a sentence as input and returns a random 500-dimensional array of floats.

    Request JSON format:
    {
        "sentence": "The input sentence."
    }

    Returns:
    JSON response:
    {
        "sentence": "The input sentence.",
        "random_array": [0.123, 0.456, ..., 0.789]
    }
    """
    if request.method == 'POST':
        try:
            data = request.get_json()
            sentence = data.get('sentence')
        except Exception as e:
            logging.error(f'Error parsing request: {e}')
            return jsonify({'message': 'Invalid request format.'}), 400
        
        # Perform input validation (example: sentence should be provided)
        if sentence is None:  # Updated condition
            logging.error('Invalid input. Sentence parameter is missing.')
            return jsonify({'message': 'Invalid input. Sentence parameter is missing.'}), 400
        
        # Generate random 500-dimensional array of floats
        random_array = np.random.rand(500).tolist()
        
        response = {
            'sentence': sentence,
            'random_array': random_array
        }
        
        logging.info(f'Request successful. Sentence: {sentence}')
        
        return jsonify(response)
    elif request.method == 'GET':
        return jsonify({'message': 'This endpoint only accepts POST requests.'}), 405
