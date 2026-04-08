# app.py

import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("marriage_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("💍 Marriage Prediction App")

st.write("Jaza taarifa hapa chini:")

# INPUTS
duration = st.number_input("Duration (years)", 0, 20)
kujimwaga = st.number_input("Effort level", 0, 50)
trust = st.number_input("Trust level", 0, 10)

helping = st.selectbox("Helping", ["no", "yes"])
fam_id = st.selectbox("Family involvement", ["low", "medium", "high"])
parent = st.selectbox("Parent support", ["no", "yes"])
finan = st.selectbox("Financial status", ["student", "employed", "stable"])

# SIMPLE ENCODING (same logic)
def encode(val, options):
    return options.index(val)

helping = encode(helping, ["no", "yes"])
fam_id = encode(fam_id, ["low", "medium", "high"])
parent = encode(parent, ["no", "yes"])
finan = encode(finan, ["student", "employed", "stable"])

# Prediction
if st.button("Predict"):
    data = np.array([[duration, kujimwaga, helping, fam_id, parent, finan, trust]])
    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("🎉 TUNAYO (Marriage likely)")
    else:
        st.error("😞 HATUNAYO (Marriage unlikely)")