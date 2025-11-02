from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return jsonify({"message":"Flask API is running"}), 200


@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", 5000)), debug=True)
