from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Root route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello World"})

# Example POST API
@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == "__main__":
    # Use environment variable PORT if set (good for Docker)
    port = int(os.environ.get("PORT", 5000))
    # debug=False for production safety
    app.run(debug=False, host="0.0.0.0", port=port)
