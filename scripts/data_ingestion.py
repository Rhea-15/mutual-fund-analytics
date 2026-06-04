import pandas as pd
from pathlib import Path

data_folder = Path(__file__).parent / "data" / "raw"

csv_files = sorted(data_folder.glob("*.csv"))

data_dict = {f.stem: pd.read_csv(f) for f in csv_files}

print("Loaded files:", list(data_dict.keys()))

for name, df in data_dict.items():
    print(f"\n" + "="*30)
    print(f"REPORT FOR: {name}")
    print("="*30)
    
    print("SHAPE (Rows, Columns)")
    print(df.shape)
    
    print("\nDATA TYPES")
    print(df.dtypes)
    
    print("\nFIRST 5 ROWS")
    print(df.head())