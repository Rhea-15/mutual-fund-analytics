# Bluestock Mutual Fund Analytics Capstone

## Overview

End-to-end mutual fund analytics platform built using Python, SQLite, Power BI and financial performance metrics.

## Objectives

* Build ETL pipeline
* Perform EDA
* Compute fund performance metrics
* Create investor analytics
* Develop recommendation engine
* Build interactive dashboard

## Project Structure
bluestone_mf_capstone
├── 📁 dashboard
│   ├── 📁 screenshots
│   │   ├── 🖼️ page1_industry_overview.png
│   │   ├── 🖼️ page2_fund_performance.png
│   │   ├── 🖼️ page3_investor_analytics.png
│   │   └── 🖼️ page4_sip_market_trends.png
│   └── 📄 bluestock_mf.pbix
├── 📁 data
│   ├── 📁 db
│   │   └── 📄 bluestock_mf.db
│   ├── 📁 processed
│   │   ├── 📄 alpha_beta.csv
│   │   ├── 📄 cagr_report.csv
│   │   ├── 📄 cohort_analysis.csv
│   │   ├── 📄 fund_scorecard.csv
│   │   ├── 📄 investor_transactions_clean.csv
│   │   ├── 📄 max_drawdown.csv
│   │   ├── 📄 nav_history_clean.csv
│   │   ├── 📄 recommendation_data.csv
│   │   ├── 📄 returns_computed.csv
│   │   ├── 📄 scheme_performance_clean.csv
│   │   ├── 📄 sector_hhi.csv
│   │   ├── 📄 sharpe_values.csv
│   │   ├── 📄 sip_continuity.csv
│   │   ├── 📄 sortino_values.csv
│   │   └── 📄 var_cvar_report.csv
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
│   ├── 📄 01_data_ingestion.ipynb
│   ├── 📄 02_data_cleaning.ipynb
│   ├── 📄 03_eda_analysis.ipynb
│   ├── 📄 05_advanced_analytics.ipynb
│   └── 📄 Performance_Analytics.ipynb
├── 📁 reports
│   └── 📁 charts
│       ├── 🖼️ age_distribution.png
│       ├── 🖼️ aum_distribution.png
│       ├── 🖼️ aum_growth.png
│       ├── 🖼️ benchmark_comparison.png
│       ├── 🖼️ category_heatmap.png
│       ├── 🖼️ city_tier_split.png
│       ├── 🖼️ correlation_heatmap.png
│       ├── 🖼️ expense_ratio_distribution.png
│       ├── 🖼️ folio_growth.png
│       ├── 🖼️ gender_distribution.png
│       ├── 🖼️ morningstar_distribution.png
│       ├── 🖼️ nav_trend.png
│       ├── 🖼️ return_vs_expense.png
│       ├── 🖼️ risk_grade_distribution.png
│       ├── 🖼️ rolling_sharpe_chart.png
│       ├── 🖼️ sector_allocation.png
│       ├── 🖼️ sector_hhi_chart.png
│       ├── 🖼️ sip_boxplot_age.png
│       ├── 🖼️ sip_trend.png
│       └── 🖼️ state_distribution.png
├── 📁 scripts
│   ├── 🐍 live_nav_fetch.py
│   ├── 🐍 load_to_sqlite.py
│   ├── 🐍 recommender.py
│   └── 🐍 run_pipeline.py
├── 📁 sql
│   ├── 📄 queries.sql
│   └── 📄 schema.sql
├── ⚙️ .gitignore
├── 📝 README.md
├── 📝 data_dictionary.md
└── 📄 requirements.txt

## Data Sources

01_fund_master.csv
02_nav_history.csv
03_aum_by_fund_house.csv
04_monthly_sip_inflows.csv
05_category_inflows.csv
06_industry_folio_count.csv
07_scheme_performance.csv
08_investor_transactions.csv
09_portfolio_holdings.csv
10_benchmark_indices.csv

## Installation

pip install -r requirements.txt

## Running ETL

python scripts/run_pipeline.py

## Dashboard

Open:
dashboard/bluestock_mf.pbix



