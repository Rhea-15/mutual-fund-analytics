import streamlit as st
import plotly.express as px
import pandas as pd

from utils import (
    load_scorecard,
    load_fund_master,
    load_nav
)

st.title("Fund Performance")

scorecard = load_scorecard()
fund_master = load_fund_master()
nav = load_nav()

df = scorecard.merge(
    fund_master,
    on="amfi_code"
)

category_filter = st.sidebar.multiselect(
    "Category",
    sorted(df["category"].dropna().unique())
)

if category_filter:
    df = df[
        df["category"].isin(category_filter)
    ]

fig = px.scatter(
    df,
    x="cagr_3yr",
    y="sharpe_ratio",
    size="fund_score",
    hover_name="scheme_name",
    title="Return vs Risk Analysis"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Fund Scorecard")

st.dataframe(
    df.sort_values(
        "fund_score",
        ascending=False
    )
)

selected_fund = st.selectbox(
    "Select Fund",
    sorted(df["scheme_name"].unique())
)

selected_code = (
    df[df["scheme_name"] == selected_fund]
    ["amfi_code"]
    .iloc[0]
)

fund_nav = nav[
    nav["amfi_code"] == selected_code
]

fig2 = px.line(
    fund_nav,
    x="date",
    y="nav",
    title="NAV Performance Over Time"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)