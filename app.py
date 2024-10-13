from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # This allows your Next.js app to make requests to the Flask server

@app.route('/api/tiles/tile1', methods=['GET'])
def get_tile1_data():
    # This is just dummy data for now
    data = {
        "title": "Tile 1",
        "content": "This is the content for Tile 1 from Flask!",
        "chartData": "Hello World"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)