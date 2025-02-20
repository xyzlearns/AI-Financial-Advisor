import streamlit as st
import requests

st.title("💰 AI Financial Advisor")

expense = st.number_input("Enter your monthly expense:", min_value=0)

if st.button("Predict Spending Category"):
    url = "http://127.0.0.1:5000/predict"
    data = {"expense": expense}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        prediction = response.json().get("prediction", "Error")
        st.success(f"📊 Prediction: {prediction}")
    else:
        st.error("⚠️ API Error! Please try again.")

