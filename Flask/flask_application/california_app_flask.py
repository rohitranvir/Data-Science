import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import joblib
from flask import Flask
app=Flask(__name__)
model=joblib.
@app.route("/")
def home():
    return ("Home")
@app.route("/predict")
def predict():
    input=[]
    for i in columns:
        val=request.args.get(i,type=int)
        input.append(val)
    ans=lr.predict(np.array([input]))
    return(ans.tolist())

if __name__=="__main__":
    app.run(debug=True)