from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

RAW = BASE_DIR / "data" / "raw"
PROCESSED = BASE_DIR / "data" / "processed"


def load_aum():
    return pd.read_csv(
        RAW / "03_aum_by_fund_house.csv"
    )


def load_sip():
    return pd.read_csv(
        RAW / "04_monthly_sip_inflows.csv"
    )


def load_category():
    return pd.read_csv(
        RAW / "05_category_inflows.csv"
    )


def load_folios():
    return pd.read_csv(
        RAW / "06_industry_folio_count.csv"
    )


def load_benchmark():
    return pd.read_csv(
        RAW / "10_benchmark_indices.csv"
    )


def load_fund_master():
    return pd.read_csv(
        RAW / "01_fund_master.csv"
    )


def load_scorecard():
    return pd.read_csv(
        PROCESSED / "fund_scorecard.csv"
    )


def load_nav():
    return pd.read_csv(
        PROCESSED / "nav_history_clean.csv"
    )


def load_transactions():
    return pd.read_csv(
        PROCESSED / "investor_transactions_clean.csv"
    )