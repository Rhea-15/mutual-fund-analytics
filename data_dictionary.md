# Data Dictionary

## Dataset: 01_fund_master.csv

| Column             | Data Type | Business Definition                       | Source      |
| ------------------ | --------- | ----------------------------------------- | ----------- |
| amfi_code          | INTEGER   | Unique AMFI scheme identifier             | fund_master |
| fund_house         | TEXT      | Mutual fund company managing the scheme   | fund_master |
| scheme_name        | TEXT      | Name of mutual fund scheme                | fund_master |
| category           | TEXT      | Broad asset category (Equity, Debt, etc.) | fund_master |
| sub_category       | TEXT      | Detailed fund classification              | fund_master |
| plan               | TEXT      | Direct or Regular plan                    | fund_master |
| launch_date        | DATE      | Scheme launch date                        | fund_master |
| benchmark          | TEXT      | Benchmark index used for comparison       | fund_master |
| expense_ratio_pct  | REAL      | Annual expense ratio percentage           | fund_master |
| exit_load_pct      | REAL      | Exit load charged on redemption           | fund_master |
| min_sip_amount     | INTEGER   | Minimum SIP investment amount             | fund_master |
| min_lumpsum_amount | INTEGER   | Minimum one-time investment amount        | fund_master |
| fund_manager       | TEXT      | Fund manager name                         | fund_master |
| risk_category      | TEXT      | Scheme risk classification                | fund_master |
| sebi_category_code | TEXT      | SEBI category code                        | fund_master |

---

## Dataset: 02_nav_history.csv

| Column    | Data Type | Business Definition      | Source      |
| --------- | --------- | ------------------------ | ----------- |
| amfi_code | INTEGER   | Scheme identifier        | nav_history |
| date      | DATE      | NAV observation date     | nav_history |
| nav       | REAL      | Net Asset Value per unit | nav_history |

---

## Dataset: 03_aum_by_fund_house.csv

| Column         | Data Type | Business Definition                     | Source            |
| -------------- | --------- | --------------------------------------- | ----------------- |
| date           | DATE      | Reporting date                          | aum_by_fund_house |
| fund_house     | TEXT      | Mutual fund company                     | aum_by_fund_house |
| aum_lakh_crore | REAL      | Assets Under Management in lakh crore   | aum_by_fund_house |
| aum_crore      | INTEGER   | Assets Under Management in crore rupees | aum_by_fund_house |
| num_schemes    | INTEGER   | Number of schemes offered               | aum_by_fund_house |

---

## Dataset: 04_monthly_sip_inflows.csv

| Column                    | Data Type | Business Definition                   | Source              |
| ------------------------- | --------- | ------------------------------------- | ------------------- |
| month                     | DATE      | Reporting month                       | monthly_sip_inflows |
| sip_inflow_crore          | INTEGER   | Monthly SIP inflows in crore rupees   | monthly_sip_inflows |
| active_sip_accounts_crore | REAL      | Active SIP accounts in crore          | monthly_sip_inflows |
| new_sip_accounts_lakh     | REAL      | Newly registered SIP accounts in lakh | monthly_sip_inflows |
| sip_aum_lakh_crore        | REAL      | SIP Assets Under Management           | monthly_sip_inflows |
| yoy_growth_pct            | REAL      | Year-over-year SIP growth percentage  | monthly_sip_inflows |

---

## Dataset: 05_category_inflows.csv

| Column           | Data Type | Business Definition                       | Source           |
| ---------------- | --------- | ----------------------------------------- | ---------------- |
| month            | DATE      | Reporting month                           | category_inflows |
| category         | TEXT      | Mutual fund category                      | category_inflows |
| net_inflow_crore | REAL      | Net inflow/outflow amount in crore rupees | category_inflows |

---

## Dataset: 06_industry_folio_count.csv

| Column              | Data Type | Business Definition   | Source               |
| ------------------- | --------- | --------------------- | -------------------- |
| month               | DATE      | Reporting month       | industry_folio_count |
| total_folios_crore  | REAL      | Total industry folios | industry_folio_count |
| equity_folios_crore | REAL      | Equity fund folios    | industry_folio_count |
| debt_folios_crore   | REAL      | Debt fund folios      | industry_folio_count |
| hybrid_folios_crore | REAL      | Hybrid fund folios    | industry_folio_count |
| others_folios_crore | REAL      | Other category folios | industry_folio_count |

---

## Dataset: 07_scheme_performance.csv

| Column             | Data Type | Business Definition                  | Source             |
| ------------------ | --------- | ------------------------------------ | ------------------ |
| amfi_code          | INTEGER   | Scheme identifier                    | scheme_performance |
| scheme_name        | TEXT      | Name of scheme                       | scheme_performance |
| fund_house         | TEXT      | Fund house name                      | scheme_performance |
| category           | TEXT      | Scheme category                      | scheme_performance |
| plan               | TEXT      | Direct or Regular plan               | scheme_performance |
| return_1yr_pct     | REAL      | One-year annualized return           | scheme_performance |
| return_3yr_pct     | REAL      | Three-year annualized return         | scheme_performance |
| return_5yr_pct     | REAL      | Five-year annualized return          | scheme_performance |
| benchmark_3yr_pct  | REAL      | Three-year benchmark return          | scheme_performance |
| alpha              | REAL      | Alpha performance metric             | scheme_performance |
| beta               | REAL      | Beta risk metric                     | scheme_performance |
| sharpe_ratio       | REAL      | Risk-adjusted return metric          | scheme_performance |
| sortino_ratio      | REAL      | Downside risk-adjusted return metric | scheme_performance |
| std_dev_ann_pct    | REAL      | Annualized standard deviation        | scheme_performance |
| max_drawdown_pct   | REAL      | Maximum historical decline           | scheme_performance |
| aum_crore          | INTEGER   | Assets Under Management in crore     | scheme_performance |
| expense_ratio_pct  | REAL      | Expense ratio percentage             | scheme_performance |
| morningstar_rating | INTEGER   | Morningstar rating score             | scheme_performance |
| risk_grade         | TEXT      | Risk classification                  | scheme_performance |

---

## Dataset: 08_investor_transactions.csv

| Column             | Data Type | Business Definition          | Source                |
| ------------------ | --------- | ---------------------------- | --------------------- |
| investor_id        | TEXT      | Unique investor identifier   | investor_transactions |
| transaction_date   | DATE      | Date of transaction          | investor_transactions |
| amfi_code          | INTEGER   | Scheme identifier            | investor_transactions |
| transaction_type   | TEXT      | SIP, Lumpsum, or Redemption  | investor_transactions |
| amount_inr         | INTEGER   | Transaction amount in INR    | investor_transactions |
| state              | TEXT      | Investor state               | investor_transactions |
| city               | TEXT      | Investor city                | investor_transactions |
| city_tier          | TEXT      | T30/B30 city classification  | investor_transactions |
| age_group          | TEXT      | Investor age group           | investor_transactions |
| gender             | TEXT      | Investor gender              | investor_transactions |
| annual_income_lakh | REAL      | Annual income in lakh rupees | investor_transactions |
| payment_mode       | TEXT      | Payment method               | investor_transactions |
| kyc_status         | TEXT      | KYC verification status      | investor_transactions |

---

## Dataset: 09_portfolio_holdings.csv

| Column            | Data Type | Business Definition             | Source             |
| ----------------- | --------- | ------------------------------- | ------------------ |
| amfi_code         | INTEGER   | Scheme identifier               | portfolio_holdings |
| stock_symbol      | TEXT      | Stock ticker symbol             | portfolio_holdings |
| stock_name        | TEXT      | Company name                    | portfolio_holdings |
| sector            | TEXT      | Industry sector                 | portfolio_holdings |
| weight_pct        | REAL      | Portfolio allocation percentage | portfolio_holdings |
| market_value_cr   | REAL      | Market value in crore rupees    | portfolio_holdings |
| current_price_inr | REAL      | Current stock price             | portfolio_holdings |
| portfolio_date    | DATE      | Portfolio reporting date        | portfolio_holdings |

---

## Dataset: 10_benchmark_indices.csv

| Column      | Data Type | Business Definition  | Source            |
| ----------- | --------- | -------------------- | ----------------- |
| date        | DATE      | Trading date         | benchmark_indices |
| index_name  | TEXT      | Benchmark index name | benchmark_indices |
| close_value | REAL      | Closing index value  | benchmark_indices |

```
```
