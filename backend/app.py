import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

# Allow backend to import from model folder
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
MODEL_DIR = os.path.join(PROJECT_ROOT, "model")

if MODEL_DIR not in sys.path:
    sys.path.append(MODEL_DIR)

from hf_client import generate_linkedin_post

app = Flask(__name__)
CORS(app)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/translate", methods=["POST"])
def translate():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON body provided"}), 400

        user_text = data.get("text", "").strip()
        mode = data.get("mode", "linkedin_cringe")

        if not user_text:
            return jsonify({"error": "Input text is required"}), 400

        result = generate_linkedin_post(user_text, mode)

        return jsonify({
            "input": user_text,
            "mode": mode,
            "output": result
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)