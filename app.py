
from pathlib import Path

import joblib
import numpy as np
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "index.html"
MODEL_FILE = BASE_DIR / "iris_model.pkl"

model = None

FEATURES = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
]

SPECIES = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica",
}


def load_model():
    global model

    if not MODEL_FILE.exists():
        print(f"ERROR: Model file not found: {MODEL_FILE.name}")
        print("Run train.py first to create the trained model.")
        return False

    try:
        model = joblib.load(MODEL_FILE)
        print("SUCCESS: Iris model loaded.")
        return True
    except Exception as error:
        print(f"ERROR: Could not load model: {error}")
        return False


@app.route("/", methods=["GET"])
def home():
    if not HTML_FILE.exists():
        return "index.html not found in the project folder.", 404

    return send_file(HTML_FILE)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "backend": "running",
        "model_loaded": model is not None
    })


@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({
            "error": "Model is not loaded. Check iris_model.pkl."
        }), 503

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Send valid JSON input."}), 400

    missing = [feature for feature in FEATURES if feature not in data]

    if missing:
        return jsonify({
            "error": "Missing measurements.",
            "missing_features": missing
        }), 400

    try:
        values = []

        for feature in FEATURES:
            value = float(data[feature])

            if not np.isfinite(value) or value <= 0:
                return jsonify({
                    "error": f"{feature} must be a positive number."
                }), 400

            values.append(value)

        # Basic sanity check for measurements in centimetres.
        if any(value > 10 for value in values):
            return jsonify({
                "error": "Measurements must be between 0 and 10 cm."
            }), 400

        input_data = np.array([values], dtype=float)

        # Real prediction from the trained model.
        prediction = model.predict(input_data)[0]

        if isinstance(prediction, (int, np.integer)):
            species = SPECIES.get(int(prediction))

            if species is None:
                return jsonify({
                    "error": "The model returned an unknown class."
                }), 500
        else:
            species = str(prediction)

        result = {
            "species": species,
            "prediction": species,
            "message": "Prediction successful"
        }

        # Include probabilities if the model supports them.
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]
            result["probabilities"] = {
                str(class_name): round(float(probability), 4)
                for class_name, probability
                in zip(model.classes_, probabilities)
            }

        return jsonify(result), 200

    except (TypeError, ValueError):
        return jsonify({
            "error": "All measurements must be valid numbers."
        }), 400

    except Exception:
        app.logger.exception("Iris prediction failed.")
        return jsonify({
            "error": "Prediction failed. Check the terminal."
        }), 500


if __name__ == "__main__":
    load_model()

    print("\nIris Flower Prediction Backend")
    print("App:    http://127.0.0.1:5000")
    print("Health: http://127.0.0.1:5000/health")
    print("API:    POST /predict\n")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
