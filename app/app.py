from flask import Flask, request, jsonify
import joblib


app = Flask(__name__)


model = joblib.load("app/model.pkl")


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    response = {'prediction': prediction.tolist()}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
