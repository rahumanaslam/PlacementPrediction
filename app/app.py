# -*- coding: utf-8 -*-
"""
    app.py: Deploying the Machine Learning Model using FastAPI
"""
__author__ = "Abdul Rahuman Aslam"
__version__ = "1.0"
__file__ = "app.py"

# Importing the required packages
import pickle
import os
from academic_record import AcademicRecord
from fastapi import FastAPI
import pandas as pd
import uvicorn

# Creating the app object from FastAPI class
app = FastAPI()

# Loading the trained model from pickle format
classifier = pickle.load(
    open(os.path.join("model", "random_forest_classifier_model_v1.pkl"), "rb")
)

# Index route, opens automatically on http://127.0.0.1:8000
@app.get("/")
def welcome():
    """
    Returns the welcome message
    """
    return {"Message": "Welcome to Placement Result Prediction"}


# Prediction Functionality Route on http://127.0.0.1:8000/api/prediction_results
@app.post("/api/prediction_results")
def predict_placement(data: AcademicRecord):
    """
    Performing the prediction on the input data and returning the result
    """
    data = data.dict()
    prediction = classifier.predict(pd.DataFrame(data))
    return {"Prediction": prediction[0]}


# Run the API with uvicorn
if __name__ == "__main__":
    """
    Main function
    """
    uvicorn.run(app, host="127.0.0.1", port=8000)
