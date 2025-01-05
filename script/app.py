from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("xgboost_final.pkl")

@app.route("/", methods=["GET"])
def health_check():
    return "API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    probabilities = model["model"].predict_proba(df)[:, 1]
    predictions = (probabilities >= model["threshold"]).astype(int)
    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
