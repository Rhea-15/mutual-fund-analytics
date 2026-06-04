from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
DB_DIR = BASE_DIR / "data" / "db"

DB_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_DIR / "bluestock_mf.db"

engine = create_engine(
    f"sqlite:///{DB_PATH}"
)

fund_df = pd.read_csv(
    RAW_DIR / "01_fund_master.csv"
)

nav_df = pd.read_csv(
    PROCESSED_DIR / "nav_history_clean.csv"
)

txn_df = pd.read_csv(
    PROCESSED_DIR / "investor_transactions_clean.csv"
)

perf_df = pd.read_csv(
    PROCESSED_DIR / "scheme_performance_clean.csv"
)

aum_df = pd.read_csv(
    RAW_DIR / "03_aum_by_fund_house.csv"
)

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("\nDatabase Loaded Successfully")

print("\nROW COUNT VALIDATION")

tables = {
    "dim_fund": len(fund_df),
    "fact_nav": len(nav_df),
    "fact_transactions": len(txn_df),
    "fact_performance": len(perf_df),
    "fact_aum": len(aum_df)
}

with engine.connect() as conn:

    for table_name, source_count in tables.items():

        db_count = conn.execute(
            text(f"SELECT COUNT(*) FROM {table_name}")
        ).scalar()

        status = (
            "MATCH"
            if source_count == db_count
            else "MISMATCH"
        )

        print(
            f"{table_name}: "
            f"CSV={source_count}, "
            f"DB={db_count} --> {status}"
        )

print("\nDatabase Location:")
print(DB_PATH)