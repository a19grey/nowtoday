import os
from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import logging
import socket
from web_scraper import scrape_url
from content_refiner import refine_content
from video_generator import generate_video
from url_validator import validate_and_normalize_url

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

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App Running</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding-top: 50px; }
            h1 { color: #4a4a4a; }
            p { color: #666; }
        </style>
    </head>
    <body>
        <h1>Flask App is Running!</h1>
        <p>The server is up and listening on port 5002.</p>
        <p>Server IP: {}</p>
        <p>Hostname: {}</p>
        <p>You can now use the /api/generate endpoint for POST requests.</p>
    </body>
    </html>
    """.format(socket.gethostbyname(socket.gethostname()), socket.gethostname())
    return render_template_string(html)

@app.route('/api/generate', methods=['POST'])
def generate():
    app.logger.info('Received request to /api/generate')
    app.logger.info(f'Request headers: {request.headers}')
    app.logger.info(f'Request body: {request.get_data(as_text=True)}')
    
    try:
        data = request.json
        url = data.get('url', '')
        app.logger.info(f'Received URL: {url}')
        
        # Validate and normalize the URL
        validated_url = validate_and_normalize_url(url)
        
        # Scrape the web page using Jina
        scraped_content = scrape_url(validated_url)
        
        # Refine the content using OpenAI
        refined_content = refine_content(scraped_content)
        
        # Generate video using HeyGen
        video_result = generate_video(refined_content)
        
        return jsonify({
            "message": f"Processing complete for URL: {validated_url}",
            "refined_content": refined_content[:100] + "...",  # Preview of refined content
            "video_result": {
                "video_url": video_result.get("video_url", ""),  # Assuming generate_video returns a dict with video_url
                "video_path": video_result.get("video_path", ""),  # Add this line
                "run_time": video_result.get("run_time", "")  # Add this line
                # Add other relevant video information here
            }
        })
    except Exception as e:
        app.logger.error(f'Error in /api/generate: {str(e)}')
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = 5002
    app.logger.info(f'Starting Flask server on port {port}')
    app.logger.info(f'Server IP: {socket.gethostbyname(socket.gethostname())}')
    app.logger.info(f'Hostname: {socket.gethostname()}')
    app.run(host='0.0.0.0', port=port, debug=True)
