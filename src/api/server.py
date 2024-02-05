from flask import Flask, jsonify, request
import pandas as pd
import joblib
from pathlib import Path

app = Flask(__name__)

# Get the absolute path of the current script
current_script_path = Path(__file__).resolve().parent

@app.route("/predict", methods=['POST'])
def do_prediction():
    json = request.get_json()
    
    relative_path = "../model/model.pkl"
    
    model_path = current_script_path / relative_path

    model = joblib.load(model_path)
    values_array = [int(value) for value in json.values()]
    x_scaled = [values_array]

    y_predict = model.predict(x_scaled)

    res = {"Estimated number of days to comaplete the task is ": round(y_predict[0],2)}
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0')