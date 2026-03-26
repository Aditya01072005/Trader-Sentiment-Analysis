# Trader Performance vs Market Sentiment Analysis

## Overview

This project analyzes the relationship between **market sentiment (Fear/Greed Index)** and **trader behavior & performance** using historical trading data from Hyperliquid.

The goal is to uncover patterns that can help design **smarter, sentiment-aware trading strategies**.

---

## Dataset

Two datasets were used:

1. **Bitcoin Market Sentiment (Fear/Greed Index)**

   * Contains daily sentiment classification (Fear, Greed, Extreme Fear, etc.)

2. **Historical Trader Data**

   * Includes trade-level data such as:

     * Account
     * Trade size
     * Side (Buy/Sell)
     * Closed PnL
     * Timestamp

---

## Data Preprocessing

* Converted timestamps to datetime format
* Extracted date for alignment
* Merged trading data with sentiment data on daily basis
* Checked for missing values and duplicates
* Observed significant missing timestamps in trade data

---

## Feature Engineering

Created key performance and behavioral metrics:

* **Daily PnL per trader**
* **Win rate**
* **Trade frequency**
* **Average trade size**
* **Sentiment-based grouping**

---

## Analysis

The analysis focused on comparing trader behavior across different sentiment conditions:

* Performance (PnL) across Fear vs Greed
* Trade frequency changes with sentiment
* Behavioral shifts in trading activity

---

## Key Insights

* Traders achieved **significantly higher profitability during Fear periods** compared to Greed.
* **Greed phases showed increased trading activity but lower returns**, indicating overtrading.
* Extreme sentiment conditions (Extreme Fear / Neutral) showed minimal activity or impact.
* Market sentiment strongly influences both **trading behavior and outcomes**.

---

## Strategy Recommendations

* **Reduce leverage during Greed periods** to avoid losses from overconfidence.
* **Capitalize on Fear periods** by focusing on high-probability trades.
* Avoid excessive trading during bullish sentiment.
* Implement **sentiment-aware trading strategies** for better risk management.
* Segment traders based on behavior (e.g., high-frequency vs low-frequency) for optimized strategies.

---

## Visualizations

The notebook includes:

* Average PnL comparison across sentiment
* Trade frequency distribution
* Behavioral trend analysis

---

## Streamlit Dashboard (Bonus)

A lightweight interactive dashboard was built using Streamlit to explore:

* Trader performance by sentiment
* Trade frequency
* Top traders

### Run Locally

```bash
streamlit run app.py
```

---

## Project Structure

```
Trader-Sentiment-Analysis/
│
├── notebook.ipynb
├── app.py
├── README.md
├── outputs/
│   ├── dashboard_1.png
│   ├── dashboard_2.png
│
└── data/
    ├── historical_data.csv
    ├── fear_greed_index.csv
```
## NOte The Dataset is not loaded because of size issue
historical_data.csv link - https://drive.google.com/file/d/1Iy9PEXdou0zk2Z3iVTfQAu5Pfv5bdy6k/view?usp=drive_link
fear_greed_index.csv - https://drive.google.com/file/d/1Z67JHnu6qVAxF3u-KiSKUJY6nR1yxORl/view?usp=drive_link

---

## Limitations

* A large number of missing timestamps were observed in the dataset.
* This may impact time-based analysis accuracy.
* Some sentiment categories had limited data coverage.

---

## Conclusion

Market sentiment plays a crucial role in trading performance.
Adapting strategies based on Fear/Greed signals can significantly improve outcomes and reduce risk.

---

## Author

Aditya Chauhan

