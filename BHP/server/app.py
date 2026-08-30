import streamlit as st
import util

# Load model
util.load_saved_artifacts()

st.set_page_config(
    page_title="Bangalore House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Bangalore House Price Prediction")
st.write("Enter the details below to estimate the house price.")

# Location
locations = util.get_location_names()

location = st.selectbox(
    "Location",
    locations
)

# Inputs
total_sqft = st.number_input(
    "Total Square Feet",
    min_value=300.0,
    max_value=10000.0,
    value=1000.0,
    step=50.0
)

bhk = st.number_input(
    "BHK",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

bath = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

# Prediction
if st.button("Predict Price"):
    try:
        price = util.get_estimated_price(
            location,
            total_sqft,
            bhk,
            bath
        )

        st.success(f"Estimated Price: ₹ {price:.2f} Lakhs")

    except Exception as e:
        st.error(f"Prediction failed: {e}")