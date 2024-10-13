from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

app = Flask(__name__)

# Update the CORS origins to only include port 3000
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000"]}})

logging.basicConfig(level=logging.DEBUG)

@app.route('/api/tiles/tile1', methods=['GET'])
def get_tile1_data():
    # This is just dummy data for now
    data = {
        "title": "Tile 1",
        "content": "This is the content for Tile 1 from Flask!",
        "chartData": "Hello World"
    }
    return jsonify(data)

@app.route('/api/generate', methods=['POST'])
def generate():
    app.logger.info('Received request')
    try:
        data = request.json
        url = data.get('url', '')
        app.logger.info(f'Received URL: {url}')
        return jsonify({"message": f"Hello World, you submitted: {url}"})
    except Exception as e:
        app.logger.error(f'Error: {str(e)}')
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
