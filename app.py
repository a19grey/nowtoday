import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

app = Flask(__name__)

# Enable CORS for all origins in development
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/api/generate', methods=['POST'])
def generate():
    app.logger.info('Received request to /api/generate')
    app.logger.info(f'Request headers: {request.headers}')
    app.logger.info(f'Request body: {request.get_data(as_text=True)}')
    
    try:
        data = request.json
        url = data.get('url', '')
        app.logger.info(f'Received URL: {url}')
        return jsonify({"message": f"Hello World, you submitted: {url}"})
    except Exception as e:
        app.logger.error(f'Error in /api/generate: {str(e)}')
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('BACKEND_PORT', 5000))
    app.logger.info(f'Starting Flask server on port {port}')
    app.run(host='0.0.0.0', port=port, debug=True)
