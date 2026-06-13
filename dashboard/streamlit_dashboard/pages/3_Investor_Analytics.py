import streamlit as st
import plotly.express as px
import pandas as pd

from utils import load_transactions

st.title("Investor Analytics")

txn = load_transactions()

state_filter = st.sidebar.multiselect(
    "State",
    sorted(txn["state"].dropna().unique())
)

if state_filter:
    txn = txn[
        txn["state"].isin(state_filter)
    ]

state_data = (
    txn.groupby("state")["amount_inr"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    state_data,
    x="state",
    y="amount_inr",
    title="Transaction Amount by State"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

split = (
    txn.groupby("transaction_type")
    ["amount_inr"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    split,
    names="transaction_type",
    values="amount_inr",
    title="SIP / Lumpsum / Redemption Split"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

age_data = (
    txn.groupby("age_group")
    ["amount_inr"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    age_data,
    x="age_group",
    y="amount_inr",
    title="Average Investment by Age Group"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

txn["month"] = (
    pd.to_datetime(
        txn["transaction_date"]
    )
    .dt.to_period("M")
    .astype(str)
)

monthly = (
    txn.groupby("month")
    ["amount_inr"]
    .sum()
    .reset_index()
)

fig4 = px.line(
    monthly,
    x="month",
    y="amount_inr",
    title="Monthly Transaction Volume"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)