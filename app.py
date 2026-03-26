import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

st.title("Trader Performance vs Market Sentiment")

# Load data
trades = pd.read_csv("historical_data.csv")
sentiment = pd.read_csv("fear_greed_index.csv")

# Clean columns
trades.columns = trades.columns.str.strip()
sentiment.columns = sentiment.columns.str.strip()

# Convert datetime
trades['Timestamp IST'] = pd.to_datetime(trades['Timestamp IST'], errors='coerce')
sentiment['date'] = pd.to_datetime(sentiment['date'], errors='coerce')

# Extract date
trades['date'] = trades['Timestamp IST'].dt.date
sentiment['date'] = sentiment['date'].dt.date

# Merge
merged = pd.merge(trades, sentiment[['date', 'classification']], on='date', how='left')

# Sidebar filter
st.sidebar.header("Filters")
sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=merged['classification'].dropna().unique(),
    default=merged['classification'].dropna().unique()
)

filtered = merged[merged['classification'].isin(sentiment_filter)]

# KPIs
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Trades", len(filtered))
col2.metric("Total PnL", round(filtered['Closed PnL'].sum(), 2))
col3.metric("Avg PnL", round(filtered['Closed PnL'].mean(), 2))

# PnL by Sentiment
st.subheader("Average PnL by Sentiment")

performance = filtered.groupby('classification')['Closed PnL'].mean()

fig, ax = plt.subplots()
performance.plot(kind='bar', ax=ax)
ax.set_ylabel("Average PnL")
st.pyplot(fig)

# Trade Frequency

st.subheader("Trade Frequency by Sentiment")

trade_freq = filtered.groupby('classification').size()

fig2, ax2 = plt.subplots()
trade_freq.plot(kind='bar', ax=ax2)
ax2.set_ylabel("Number of Trades")
st.pyplot(fig2)


# Top Traders

st.subheader("Top Traders by PnL")

top_traders = filtered.groupby('Account')['Closed PnL'].sum().sort_values(ascending=False).head(10)

st.dataframe(top_traders)

st.write("Built with using Streamlit")