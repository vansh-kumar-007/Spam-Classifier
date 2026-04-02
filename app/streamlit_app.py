import streamlit as st
import requests

# API URL
API_URL = "https://spam-classifier-ps0y.onrender.com//predict"

st.set_page_config(page_title="Spam Classifier", page_icon="📩")

st.title("📩 Spam Classifier")
st.write("Enter a message to check whether it is Spam or Ham")

# Input box
message = st.text_area("Enter your message:")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message")
    else:
        # Send request to API
        response = requests.post(API_URL, json={"message": message})
        
        if response.status_code == 200:
            result = response.json()
            
            prediction = result["prediction"]
            probability = result["probability"]
            
            if prediction == "Spam":
                st.error(f"🚨 Spam ({probability:.2f})")
            else:
                st.success(f"✅ Ham ({probability:.2f})")
        else:
            st.error("Error connecting to API")