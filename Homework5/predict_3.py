from flask import Flask, request

from predict import load, predict

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def hello_world():
    input_features = request.json
    dv = load("data/dv.bin")
    model = load("data/model.bin")
    y_pred = predict(dv, model, input_features)

    return {"prediction": y_pred[0]}