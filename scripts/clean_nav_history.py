import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# -----------------------------
# 1. Convert Date Column
# -----------------------------
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

invalid_dates = df["date"].isna().sum()

print("\nInvalid Dates:", invalid_dates)

# -----------------------------
# 2. Sort Data
# -----------------------------
df = df.sort_values(
    ["amfi_code", "date"]
)

print("\nData sorted by amfi_code and date")

# -----------------------------
# 3. Remove Duplicate Rows
# -----------------------------
duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

if duplicates > 0:
    print("Removing duplicate rows...")
    df = df.drop_duplicates()

# -----------------------------
# 4. Forward Fill NAV Values
# -----------------------------
missing_before = df["nav"].isna().sum()

print("\nMissing NAV Before Fill:", missing_before)

df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

missing_after = df["nav"].isna().sum()

print("Missing NAV After Fill:", missing_after)

# -----------------------------
# 5. Validate NAV > 0
# -----------------------------
invalid_nav = (df["nav"] <= 0).sum()

print("\nInvalid NAV Values:", invalid_nav)

if invalid_nav > 0:
    print("Removing invalid NAV rows...")
    df = df[df["nav"] > 0]

# -----------------------------
# 6. Final Validation
# -----------------------------
print("\nFinal Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

df.to_csv(
    "../data/processed/nav_history_clean.csv",
    index=False
)