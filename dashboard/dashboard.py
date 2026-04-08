"""
Dashboard to see live crypto prices, watch them update and interact with the data
"""

import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
import time

def load_data():
    conn = mysql.connector.connect( host="localhost",port=3307,user="root",password="root", database="crypto_db")

    query = """
    SELECT symbol, price_usd, fetched_at
    FROM crypto_prices
    ORDER BY fetched_at DESC
    LIMIT 100;
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("Real-Time Crypto Dashboard")

df = load_data()
if df.empty:
    st.warning("No data found. Make sure producer & consumer are running.")
    st.stop()

coin = st.selectbox("Select Coin", df["symbol"].unique())

filtered = df[df["symbol"] == coin].sort_values("fetched_at")

# big display, % change indicator, trading dashboard
latest_price = filtered.iloc[-1]["price_usd"]
prev_price = filtered.iloc[-2]["price_usd"]

change = ((latest_price - prev_price) / prev_price) * 100

st.metric(label=f"{coin} Current Price", value=f"${latest_price:.2f}", delta=f"{change:.2f}%")

if abs(change) > 1:
    st.error(f"!!!Alert!!! : {coin} changed {change:.2f}%!")


fig = px.line(filtered, x="fetched_at", y="price_usd", title=f"{coin} Price")
st.plotly_chart(fig)

# refresh every 5 seconds and pull new db data
time.sleep(5)
st.rerun()