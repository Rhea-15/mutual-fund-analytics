import streamlit as st

st.set_page_config(
    page_title="Bluestock MF Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("Bluestock Mutual Fund Analytics Dashboard")

st.markdown("""
### Navigation

Use the sidebar to explore:

- Industry Overview
- Fund Performance
- Investor Analytics
- SIP & Market Trends
""")