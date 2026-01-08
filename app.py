from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS
import numpy as np
from datetime import datetime

model_path = 'XGBmodel.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_all', methods=['POST'])
def predict():
    today = datetime.today()

    # Monday=1, Sunday=7
    day_num = today.weekday() + 1
    weekend = 1 if day_num in [6, 7] else 0

    # Feature vector (MUST match model training order)
    features = np.array([[weekend, day_num, weekend**2, day_num**2, 0, 0]])

    prediction = model.predict(features)
    prediction_rounded = np.round(prediction).astype(int).tolist()

    return jsonify({
    "prediction":prediction_rounded[0],
    "day_num":day_num,
    "weekend":weekend
    })


if __name__ == "__main__":
    app.run(debug=True)