import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request
import joblib


app = Flask(__name__)


with open("model.pkl", "rb") as f:
    saved_model = pickle.load(f)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    cylinders = request.form.get("cylinders", None)
    displacement = request.form.get("displacement", None)
    horsepower = request.form.get("horsepower", None)
    weight = request.form.get("weight", None)
    acceleration = request.form.get("acceleration", None)
    model_year = request.form.get("model_year", None)
    origin = request.form.get("origin", None)

    # Check if any data is None
    if any(value is None for value in [cylinders, displacement, horsepower, weight, acceleration, model_year, origin]):
        return jsonify({'error': -999})

    # Convert the values to float and use -999 if not provided
    data = [
        float(cylinders) if cylinders is not None else -999,
        float(displacement) if displacement is not None else -999,
        float(horsepower) if horsepower is not None else -999,
        float(weight) if weight is not None else -999,
        float(acceleration) if acceleration is not None else -999,
        float(model_year) if model_year is not None else -999,
        float(origin) if origin is not None else -999
    ]

    # Make predictions using the model
    prediction = saved_model.predict([data])[0]

    return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True, port= 5002)


