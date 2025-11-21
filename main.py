import pandas as pd
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Load CSV and extract unique locations
data = pd.read_csv('Cleaned_data.csv')
locations = sorted(data['location'].unique())  # assuming column name 'location'

@app.route('/')
def home():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    location = request.form['location']
    sqft = float(request.form['sqft'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # Dummy prediction logic (replace with real model later)
    price = sqft * 3000 + bhk * 50000 + bath * 30000

    return str(round(price, 2))

if __name__ == "__main__":
    app.run(debug=True)
