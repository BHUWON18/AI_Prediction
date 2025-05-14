from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('models/best_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict exact number of goals
def predict_goals(features):
    prediction = model.predict([features])
    return prediction[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the user
    assists = float(request.form['assists'])
    completed_pass = float(request.form['completed_pass'])
    goals_scored = float(request.form['goals_scored'])
    assists_per_90 = float(request.form['assists_per_90'])
    
    # Prepare input for prediction
    features = [assists, completed_pass, goals_scored, assists_per_90]
    
    # Get prediction (exact number of goals)
    predicted_goals = predict_goals(features)
    
    return render_template('index.html', predicted_goals=predicted_goals)

if __name__ == '__main__':
    app.run(debug=True)
