import streamlit as st
import plotly.express as px
import pandas as pd

from utils import (
    load_aum,
    load_sip,
    load_folios
)

st.title("Industry Overview")

aum = load_aum()
sip = load_sip()
folios = load_folios()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total AUM (L Cr)",
    round(aum["aum_lakh_crore"].max(), 2)
)

col2.metric(
    "SIP Inflow (Cr)",
    round(sip["sip_inflow_crore"].max(), 0)
)

col3.metric(
    "Folios (Cr)",
    round(folios["total_folios_crore"].max(), 2)
)

col4.metric(
    "Schemes",
    int(aum["num_schemes"].max())
)

industry_aum = (
    aum.groupby("date")["aum_lakh_crore"]
    .sum()
    .reset_index()
)

fig = px.line(
    industry_aum,
    x="date",
    y="aum_lakh_crore",
    title="Industry AUM Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

latest_date = aum["date"].max()

top_amc = (
    aum[aum["date"] == latest_date]
    .sort_values(
        "aum_lakh_crore",
        ascending=False
    )
    .head(10)
)

fig2 = px.bar(
    top_amc,
    x="fund_house",
    y="aum_lakh_crore",
    title="Top 10 AMC by AUM"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)