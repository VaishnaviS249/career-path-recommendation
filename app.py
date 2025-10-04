import streamlit as st
import joblib

st.title("🎯 Career Path Recommendation System")
st.write("Get personalized career suggestions based on your skills!")

# Load model and encoder
model = joblib.load('career_model.pkl')
le = joblib.load('label_encoder.pkl')

# Inputs
math = st.slider("Math Skill (1-10)", 1, 10, 5)
coding = st.slider("Coding Skill (1-10)", 1, 10, 5)
communication = st.slider("Communication Skill (1-10)", 1, 10, 5)

# Prediction
if st.button("Predict Career"):
    data = [[math, coding, communication]]
    pred = model.predict(data)
    career = le.inverse_transform(pred)[0]
    st.success(f"💼 Recommended Career Path: **{career}**")
