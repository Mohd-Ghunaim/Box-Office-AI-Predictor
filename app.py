from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os
from dotenv import load_dotenv
from tmdb_utils import get_movie_features

# Load environment variables
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    title = data.get("title")

    if not title:
        return jsonify({"error": "Missing title"}), 400

    try:
        features_df = get_movie_features(title, TMDB_API_KEY)
        prediction = model.predict(features_df)[0]

        return jsonify({
            "title": title,
            "predicted_revenue": float(round(prediction, 2))
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Use Render's PORT environment variable, default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
