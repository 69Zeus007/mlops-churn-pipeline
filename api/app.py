from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('models/churn_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([[
        data['tenure'],
        data['MonthlyCharges'],
        data['TotalCharges']
    ]])
    prediction = model.predict(features)[0]
    return jsonify({'churn_prediction': int(prediction)})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'API is running'})

if __name__ == '__main__':
    app.run(debug=True)