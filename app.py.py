import streamlit as st
import joblib

# Load complete pipeline
pipeline = joblib.load("mood_pipeline.pkl")

st.title("🧠 AI Mood Detector")

text = st.text_input("Enter your feeling:")

if st.button("Predict Mood"):

    if text:
        prediction = pipeline.predict([text])[0]

        st.success(f"Predicted Mood: {prediction}")

    else:
        st.warning("Please enter text")
