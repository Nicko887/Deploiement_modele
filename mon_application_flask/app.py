from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = "http://127.0.0.1:8000/score"  # Assurez-vous que cette URL est correcte pour votre API de prédiction
    response = requests.post(url, json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
