import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from utils import (
    load_sip,
    load_category,
    load_benchmark
)

st.title("SIP & Market Trends")

sip = load_sip()
category = load_category()
benchmark = load_benchmark()

fig = go.Figure()

fig.add_bar(
    x=sip["month"],
    y=sip["sip_inflow_crore"],
    name="SIP Inflow"
)

nifty = benchmark[
    benchmark["index_name"]
    .str.contains(
        "Nifty",
        case=False,
        na=False
    )
]

fig.add_scatter(
    x=nifty["date"],
    y=nifty["close_value"],
    mode="lines",
    name="Nifty"
)

fig.update_layout(
    title="SIP Inflow vs Nifty"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader(
    "Category Inflow Heatmap"
)

heatmap = category.pivot_table(
    values="net_inflow_crore",
    index="category",
    columns="month"
)

st.dataframe(heatmap)

top5 = (
    category.groupby("category")
    ["net_inflow_crore"]
    .sum()
    .reset_index()
    .sort_values(
        "net_inflow_crore",
        ascending=False
    )
    .head(5)
)

fig2 = px.bar(
    top5,
    x="category",
    y="net_inflow_crore",
    title="Top Categories by Net Inflow"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)