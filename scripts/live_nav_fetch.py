import os
import requests
import pandas as pd

os.makedirs("data/raw", exist_ok=True)

hdfc_url = "https://api.mfapi.in/mf/125497"

try:
    print("Fetching HDFC Top 100 Direct...")
    response = requests.get(hdfc_url, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        if "data" in data and data["data"]:
            nav_df = pd.DataFrame(data["data"])
            nav_df.to_csv("data/raw/HDFC_Top100_Direct.csv", index=False)
            print("✓ HDFC Top 100 Direct saved")
        else:
            print("⚠ HDFC URL returned success but no data payload found.")
    else:
        print(f"⚠ Failed to fetch HDFC. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("\nWarning: HDFC Live NAV fetch failed due to a network connection issue.")
    print(f"Details: {e}")
    print("Proceeding with pipeline execution stability...\n")


funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in funds.items():
    print(f"\nFetching {name} ({code})...")
    try:
        url = f"https://api.mfapi.in/mf/{code}"
        response = requests.get(url, timeout=10)
        print("Status:", response.status_code)

        if response.status_code != 200:
            print("Failed")
            continue

        data = response.json()

        if "data" not in data or not data["data"]:
            print("No NAV data found")
            continue

        df = pd.DataFrame(data["data"])
        df.to_csv(f"data/raw/{name}.csv", index=False)
        print("Saved")

    except requests.exceptions.RequestException as e:
        print(f"Network Error fetching {name}: {e}")
    except Exception as e:
        print(f"Unexpected Error processing {name}: {e}")

print("\nProcessing for live_nav_fetch.py finished.")