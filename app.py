import streamlit as st
import pandas as pd
import joblib
import os

print(os.listdir())
# Load Model
model = joblib.load(
    "attrition_model_v2.pkl"
)

THRESHOLD = 0.40

st.set_page_config(
    page_title="Employee Attrition Predictor",
    layout="wide"
)

st.title("AI Powered Employee Attrition Prediction System")

st.write(
    "Predict employee attrition risk using Machine Learning"
)
