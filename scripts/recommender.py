from pathlib import Path
import pandas as pd

base = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    base / "data" / "processed" / "recommendation_data.csv"
)

risk = input(
    "Enter risk appetite (Low/Moderate/High): "
)

filtered = df[
    df["risk_category"]
    .str.contains(
        risk,
        case=False,
        na=False
    )
]

top3 = (
    filtered
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop Recommended Funds\n")

print(
    top3[
        [
            "scheme_name",
            "sharpe_ratio",
            "fund_score"
        ]
    ]
)