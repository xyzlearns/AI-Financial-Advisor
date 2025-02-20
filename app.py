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
    app.run(debug=True)