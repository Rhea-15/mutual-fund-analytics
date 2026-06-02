# Mutual Fund Analytics Platform

## Overview

A data analytics project focused on Indian mutual funds. The project combines historical NAV data, fund metadata, investor transactions, AUM trends, SIP inflows, and benchmark indices to generate insights into fund performance and investor behavior.

## Project Structure

mutual-fund-analytics/

├── 📁 dashboard
├── 📁 data
│   ├── 📁 processed
│   └── 📁 raw
│       ├── 📄 01_fund_master.csv
│       ├── 📄 02_nav_history.csv
│       ├── 📄 03_aum_by_fund_house.csv
│       ├── 📄 04_monthly_sip_inflows.csv
│       ├── 📄 05_category_inflows.csv
│       ├── 📄 06_industry_folio_count.csv
│       ├── 📄 07_scheme_performance.csv
│       ├── 📄 08_investor_transactions.csv
│       ├── 📄 09_portfolio_holdings.csv
│       ├── 📄 10_benchmark_indices.csv
│       ├── 📄 Axis_Bluechip.csv
│       ├── 📄 HDFC_Top100_Direct.csv
│       ├── 📄 ICICI_Bluechip.csv
│       ├── 📄 Kotak_Bluechip.csv
│       ├── 📄 Nippon_Large_Cap.csv
│       └── 📄 SBI_Bluechip.csv
├── 📁 notebooks
├── 📁 reports
├── 📁 sql
├── ⚙️ .gitignore
├── 📝 README.md
├── 🐍 amfi_validation.py
├── 🐍 data_ingestion.py
├── 🐍 explore_fund_master.py
├── 🐍 live_nav_fetch.py
└── 📄 requirements.txt

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* Requests
* SciPy
* Git & GitHub

## Setup

Clone the repository:
git clone <repository-url>

Install dependencies:
pip install -r requirements.txt

Run data ingestion:
python data_ingestion.py

Run NAV fetch:
python live_nav_fetch.py

Explore fund master metadata:
python explore_fund_master.py

Validate AMFI codes:
python amfi_validation.py
