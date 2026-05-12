import streamlit as st
import requests


st.set_page_config(

    page_title="MarketMix Intelligence Platform",

    layout="wide"
)


st.title(
    "MarketMix Intelligence Platform"
)

st.markdown(
    "ML-Powered Marketing Revenue Prediction System"
)


st.sidebar.header("Campaign Inputs")


spend = st.sidebar.number_input(
    "Marketing Spend",
    min_value=0,
    value=2500
)

impressions = st.sidebar.number_input(
    "Impressions",
    min_value=0,
    value=120000
)

clicks = st.sidebar.number_input(
    "Clicks",
    min_value=0,
    value=12000
)

conversions = st.sidebar.number_input(
    "Conversions",
    min_value=0,
    value=800
)

ctr = st.sidebar.number_input(
    "CTR",
    min_value=0.0,
    value=10.0
)

roas = st.sidebar.number_input(
    "ROAS",
    min_value=0.0,
    value=4.5
)


if st.button("Predict Revenue"):

    url = "https://market-mix-intelligence-platform.onrender.com/predict"
    params = {

        "spend": spend,

        "impressions": impressions,

        "clicks": clicks,

        "conversions": conversions,

        "ctr": ctr,

        "roas": roas
    }

    response = requests.post(
        url,
        params=params
    )

    prediction = response.json()

    st.success(
        f"Predicted Revenue: ₹ {prediction['predicted_revenue']}"
    )

    st.metric(
        label="Predicted Revenue",

        value=f"₹ {prediction['predicted_revenue']}"
    )

    st.balloons()