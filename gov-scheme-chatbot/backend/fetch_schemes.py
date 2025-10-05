# backend/fetch_schemes.py
import requests
import json
import os

RESOURCE_ID = "579b464db66ec23bdd000001d51cebf082444cda65a212b2295dc30b"
API_KEY = "579b464db66ec23bdd000001d51cebf082444cda65a212b2295dc30b"

API_URL = f"https://api.data.gov.in/resource/{RESOURCE_ID}?api-key={API_KEY}&format=json"
OUTPUT_FILE = os.path.join("data", "schemes.json")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python Script"
}

def fetch_and_save_data():
    try:
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            data = response.json()
            records = data.get("records", [])  # <-- Only take the records
            os.makedirs("data", exist_ok=True)
            with open(OUTPUT_FILE, "w", encoding='utf-8') as f:
                json.dump(records, f, indent=4, ensure_ascii=False)
            print("✅ Data saved to", OUTPUT_FILE)
        else:
            print(f"❌ Failed to fetch data. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print("❌ Error occurred:", e)

if __name__ == "__main__":
    fetch_and_save_data()
