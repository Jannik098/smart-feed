import pandas as pd
import numpy as np
from scipy.optimize import minimize
import streamlit as st

feed_data = {
    "cereals": {"emission_factor": 0.35, "raw_protein": 0.10},
    "soy_eu": {"emission_factor": 0.95, "raw_protein": 0.45},
    "soy_non_eu": {"emission_factor": 4.35, "raw_protein": 0.45},
    "rapeseed": {"emission_factor": 0.66, "raw_protein": 0.35},
    "mineral_feed": {"emission_factor": 1.25, "raw_protein": 0.00},
}

feed_df = pd.DataFrame.from_dict(feed_data, orient="index")

# Streamlit: Input field for raw protein of the mixed feed
st.header("Farmer Input: Mixed Feed Raw Protein")

# Farmer inputs the raw protein percentage (e.g., 22%)
raw_protein_input = st.number_input(
    "Enter the raw protein content of your mixed feed (%)",
    min_value=0.0,
    max_value=100.0,
    value=22.0,  # Default value
    step=0.1,  # Increment step
    format="%.1f"
)

# Display the entered value
st.write(f"Raw protein content entered: {raw_protein_input:.1f}%")


# Streamlit: Feed Category Selection

st.header("Farmer Input: Feed Category Selection")

# Predefined list of feed categories
feed_categories = ["cereal", "soy eu", "soy non-eu", "rapeseed", "mineral feed"]

# Initialize or retrieve session state for the selected feed order
if "feed_order" not in st.session_state:
    st.session_state.feed_order = []

# Add feed category to the order
selected_feed = st.selectbox("Select a feed category to add:", options=feed_categories)
if st.button("Add Category"):
    st.session_state.feed_order.append(selected_feed)

# Remove the last feed category
if st.button("Remove Last Category"):
    if st.session_state.feed_order:
        st.session_state.feed_order.pop()

# Display the current order of feeds
st.subheader("Current Feed Order:")
if st.session_state.feed_order:
    for idx, feed in enumerate(st.session_state.feed_order, start=1):
        st.write(f"{idx}. {feed}")
else:
    st.write("No feed categories added yet.")

# Add a Reset Button
if st.button("Reset Feed Order"):
    st.session_state.feed_order = []