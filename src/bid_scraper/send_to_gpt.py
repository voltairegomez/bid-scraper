import os
import json
import requests
from normalizers_planetbids import normalize_planetbids
from storage import save_opportunity


API_URL = os.getenv("GPT_ENDPOINT_URL", "http://127.0.0.1:8000/api/opportunities")


def send_to_gpt(normalized):
    """Send a normalized Opportunity to the GPT for analysis and scoring."""
    headers = {"Content-Type": "application/json"}
    data = normalized.to_json()
    saved_path = save_opportunity(data)
    print(f"Saved normalized JSON to: {saved_path}")

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    print(f"Status: {response.status_code}")
    print(response.text)


if __name__ == "__main__":
    # Example using your sample raw data
    raw = {
        "agency": "City of Sampleville",
        "title": "Office Furniture Procurement",
        "number": "RFP-2025-001",
        "type": "RFP",
        "timezone": "America/Los_Angeles",
        "due_iso": "2025-01-30T14:00:00-08:00",
        "submission": "Online via PlanetBids portal",
        "summary": "Procurement of ergonomic office furniture and installation."
    }

    normalized = normalize_planetbids(raw)
    send_to_gpt(normalized)
