import pickle

def load(path):
    with open(path, "rb") as read_file:
        unpickled = pickle.load(read_file)

    return unpickled

def predict(dv, model, features):
    X = dv.transform(features)
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred

def main(features):
    dv = load("data/dv.bin")
    model = load("data/model.bin")
    y_pred = predict(dv, model, features)
    print("Credit probability is", y_pred[0])

if __name__ == "__main__":
    input_features = {"job": "retired", "duration": 445, "poutcome": "success"}
    main(input_features)