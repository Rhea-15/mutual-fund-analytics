import requests
import pandas as pd

hdfc_url = "https://api.mfapi.in/mf/125497"

response = requests.get(hdfc_url)

if response.status_code == 200:
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        "data/raw/HDFC_Top100_Direct.csv",
        index=False
    )

    print("HDFC Top 100 Direct saved")


funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in funds.items():

    print(f"\nFetching {name} ({code})")

    try:
        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url, timeout=10)

        print("Status:", response.status_code)

        if response.status_code != 200:
            print("Failed")
            continue

        data = response.json()

        if "data" not in data:
            print("No NAV data found")
            continue

        df = pd.DataFrame(data["data"])

        df.to_csv(
            f"data/raw/{name}.csv",
            index=False
        )

        print("Saved")

    except Exception as e:
        print("Error:", e)