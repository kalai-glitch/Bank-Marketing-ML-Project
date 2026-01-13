from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load model and scaler
model = joblib.load("bank_model.joblib")
scaler = joblib.load("scaler.joblib")

# Homepage route with a simple form
@app.route('/')
def home():
    return '''
    <h2>Bank Marketing Prediction</h2>
    <form action="/predict" method="post">
        Age: <input type="number" name="age"><br>
        Balance: <input type="number" name="balance"><br>
        Duration: <input type="number" name="duration"><br>
        # Add more input fields here as per your dataset features
        <input type="submit" value="Predict">
    </form>
    '''

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data and convert to float
        age = float(request.form['age'])
        balance = float(request.form['balance'])
        duration = float(request.form['duration'])
        # Add more features here

        # Create feature array
        features = np.array([[age, balance, duration]]) # add more features in same order
        # Scale features
        features_scaled = scaler.transform(features)
        # Predict
        prediction = model.predict(features_scaled)

        # Return result
        return f"<h3>Prediction: {'Yes' if prediction[0]==1 else 'No'}</h3>"

    except Exception as e:
        return str(e)

# API version (optional)
@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()
    try:
        features = np.array([[
            data['age'],
            data['balance'],
            data['duration']
# Add other features here
        ]])
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
