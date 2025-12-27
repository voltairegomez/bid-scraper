import os, json, sys, requests
from normalizers_planetbids import normalize_planetbids
from storage import save_opportunity

API_URL = os.getenv("GPT_ENDPOINT_URL", "http://127.0.0.1:8000/api/opportunities")

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m bid_scraper.cli path/to/raw_planetbids.json")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        raw = json.load(f)
    opp = normalize_planetbids(raw)
    data = opp.to_json()
    path = save_opportunity(data)
    print(f"Saved: {path}")
    r = requests.post(API_URL, headers={"Content-Type":"application/json"}, data=json.dumps(data))
    print(f"Status: {r.status_code}")
    print(r.text)

if __name__ == "__main__":
    main()
