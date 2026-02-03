import os
import time
import requests
import streamlit as st

st.set_page_config(page_title="House Price Predictor", layout="wide")
st.title("House Price Prediction")

API_URL = os.getenv("API_URL", "http://fastapi:8000").rstrip("/")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

with st.sidebar:
    st.write("Config")
    st.write(f"API_URL: {API_URL}")
    st.write(f"APP_VERSION: {APP_VERSION}")

col1, col2 = st.columns(2)

with col1:
    sqft = st.slider("Square Footage", 500, 5000, 1500, 50)
    bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5, 6], index=2)
    bathrooms = st.selectbox("Bathrooms", [1, 1.5, 2, 2.5, 3, 3.5, 4], index=2)
    location = st.selectbox("Location", ["urban", "suburban", "rural", "waterfront", "mountain"], index=1)
    year_built = st.slider("Year Built", 1900, 2025, 2000, 1)
    predict = st.button("Predict")

with col2:
    st.subheader("Prediction Results")

    if predict:
        payload = {
            "sqft": sqft,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "location": location,
            "year_built": year_built,
            "condition": "Good",
        }

        try:
            with st.spinner("Calling prediction API..."):
                t0 = time.time()
                r = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
                r.raise_for_status()
                data = r.json()
                elapsed = time.time() - t0

            st.success(f"OK ({elapsed:.2f}s)")
            st.json(data)

        except Exception as e:
            st.error(f"API error: {e}")
            st.info("Showing mock demo output.")
            st.json(
                {
                    "predicted_price": 467145,
                    "confidence_interval": [420430.5, 513859.5],
                    "features_importance": {"sqft": 0.43, "location": 0.27, "bathrooms": 0.15},
                }
            )

st.caption(f"Version: {APP_VERSION}")
