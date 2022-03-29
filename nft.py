import streamlit as st
import requests, json

st.sidebar.header("Endpoints")
endpoint_choices = ['Collections', 'Assets']
endpoint = st.sidebar.selectbox("Choose an Endpoint", endpoint_choices)

st.title(f"OpenSea Tracker - {endpoint}")

if endpoint == 'Assets':
    url = "https://api.opensea.io/api/v1/assets?order_direction=desc&limit=20&include_orders=false"
    headers = {
        "Accept": "application/json",
        "X-API-KEY": "No"
    }
    response = requests.request("GET", url, headers=headers)
    st.write(response.text)

if endpoint == 'Collections':
    collection = st.sidebar.text_input("Collection")
    headers = {"Accept": "application/json"}
    url = "https://api.opensea.io/api/v1/collection/{}/stats".format(collection)
    response = requests.get(url, headers=headers)
    values = ["num_owners", "average_price", "total_sales", "total_volume", "total_supply", "floor_price"]
    st.write(json.loads(response.text))
    