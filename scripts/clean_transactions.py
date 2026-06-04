import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# -----------------------------
# 1. Fix Date Format
# -----------------------------
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Check invalid dates
invalid_dates = df["transaction_date"].isna().sum()
print("Invalid Dates:", invalid_dates)

# -----------------------------
# 2. Standardize Transaction Types
# -----------------------------
print("\nTransaction Types Before:")
print(df["transaction_type"].unique())

df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.lower()
)

mapping = {
    "sip": "SIP",
    "lumpsum": "Lumpsum",
    "redemption": "Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
    .replace(mapping)
)

print("\nTransaction Types After:")
print(df["transaction_type"].unique())

# -----------------------------
# 3. Validate Amount > 0
# -----------------------------
invalid_amounts = (df["amount_inr"] <= 0).sum()

print("\nInvalid Amounts:", invalid_amounts)

if invalid_amounts > 0:
    print("Removing invalid amount rows...")
    df = df[df["amount_inr"] > 0]

# -----------------------------
# 4. Check KYC Status Values
# -----------------------------
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

allowed_kyc = [
    "Verified",
    "Pending"
]

invalid_kyc = df[
    ~df["kyc_status"].isin(allowed_kyc)
]

print("Invalid KYC Records:", len(invalid_kyc))

# -----------------------------
# 5. Remove Duplicate Rows
# -----------------------------
duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

if duplicates > 0:
    df = df.drop_duplicates()

# -----------------------------
# 6. Final Validation
# -----------------------------
print("\nFinal Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())


df.to_csv(
    "../data/processed/investor_transactions_clean.csv",
    index=False
)

