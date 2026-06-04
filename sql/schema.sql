-- Dimension Table: Fund

CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    fund_manager TEXT,
    risk_category TEXT
);

-- Dimension Table: Date

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE UNIQUE,
    year INTEGER,
    month INTEGER,
    quarter INTEGER
);

-- Fact Table: NAV

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date DATE,
    nav REAL,
    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

-- Fact Table: Transactions

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    kyc_status TEXT,
    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

-- Fact Table: Performance

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    expense_ratio_pct REAL,
    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

-- Fact Table: AUM

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    date DATE,
    aum_crore REAL,
    num_schemes INTEGER
);