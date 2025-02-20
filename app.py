from flask import Flask, request, jsonify
from model import predict_spending

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    expense = data.get("expense", 0)

    prediction = predict_spending(expense)  # Use ML model

    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    from waitress import serve
    import os
port = int(os.environ.get("PORT", 8080))  # Use PORT from environment or default to 8080
serve(app, host="0.0.0.0", port=port)

