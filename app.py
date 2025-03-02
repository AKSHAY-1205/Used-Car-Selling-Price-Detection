import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("models/random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("🚗 Car Selling Price Prediction 💰")

# User inputs
year = st.number_input("Year of Purchase", min_value=1990, max_value=2024, step=1)
km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, step=1000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
present_price = st.number_input("Present Price (Lakhs)", min_value=0.0, max_value=50.0, step=0.1)

# Include "Owner" feature if present in the training data
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])  # Add this to match model training

# Encode categorical inputs
fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2, "Electric": 3}
seller_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 0, "Automatic": 1}

# Prepare feature array
features = np.array([
    [year, km_driven, present_price, fuel_map[fuel_type], seller_map[seller_type], trans_map[transmission], owner]
])  # Ensure this matches model training

# Predict price
if st.button("Predict Price"):
    predicted_price = model.predict(features)
    st.success(f"Estimated Selling Price: ₹{predicted_price[0]:,.2f}")
