import numpy as np
import joblib
from flask import Flask, request

app = Flask(__name__)

model = joblib.load("california_model.joblib")

columns = [
    "MedInc", "HouseAge", "AveRooms", "AveBedrms",
    "Population", "AveOccup", "Latitude", "Longitude"
]

@app.route("/")
def home():
    return "California Housing prediction"

@app.route("/predict", methods=["GET"])
def predict():
    input_data = []

    for i in columns:
        val = request.args.get(i, type=float)
        if val is None:
            return f"Missing value for {i}"
        input_data.append(val)

    ans = model.predict(np.array([input_data]))
    return str(ans.tolist())

if __name__ == "__main__":
    app.run(debug=True)