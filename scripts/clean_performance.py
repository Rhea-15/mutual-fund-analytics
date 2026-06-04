import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# -----------------------------
# 1. Validate Return Columns
# -----------------------------
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

    invalid_count = df[col].isna().sum()

    print(f"\nInvalid values in {col}:",
          invalid_count)

# -----------------------------
# 2. Check Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# 3. Validate Expense Ratio
# -----------------------------
expense_anomalies = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print(
    "\nExpense Ratio Anomalies:",
    len(expense_anomalies)
)

if len(expense_anomalies) > 0:

    print("\nAnomalous Records:")

    print(
        expense_anomalies[
            [
                "scheme_name",
                "expense_ratio_pct"
            ]
        ]
    )

# -----------------------------
# 4. Flag Return Anomalies
# -----------------------------
return_anomalies = df[
    (df["return_1yr_pct"] < -100)
    |
    (df["return_1yr_pct"] > 100)
    |
    (df["return_3yr_pct"] < -100)
    |
    (df["return_3yr_pct"] > 100)
    |
    (df["return_5yr_pct"] < -100)
    |
    (df["return_5yr_pct"] > 100)
]

print(
    "\nReturn Value Anomalies:",
    len(return_anomalies)
)

if len(return_anomalies) > 0:

    print("\nAnomalous Return Records:")

    print(
        return_anomalies[
            [
                "scheme_name",
                "return_1yr_pct",
                "return_3yr_pct",
                "return_5yr_pct"
            ]
        ]
    )

# -----------------------------
# 5. Remove Duplicate Rows
# -----------------------------
duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

if duplicates > 0:

    print("Removing duplicate rows...")

    df = df.drop_duplicates()

# -----------------------------
# 6. Final Validation
# -----------------------------
print("\nFinal Shape:", df.shape)

print("\nData Types:")
print(df.dtypes)


df.to_csv(
    "../data/processed/scheme_performance_clean.csv",
    index=False
)

