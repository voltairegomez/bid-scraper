from normalizers_planetbids import normalize_planetbids

# Example raw PlanetBids-style data
sample_raw = {
    "agency": "City of Sampleville",
    "title": "Office Furniture Procurement",
    "number": "RFP-2025-001",
    "type": "RFP",
    "timezone": "America/Los_Angeles",
    "due_iso": "2025-01-30T14:00:00-08:00",
    "submission": "Online via PlanetBids portal",
    "summary": "Procurement of ergonomic office furniture and installation.",
    "required_docs": ["Attachment A - Price Sheet.xlsx"],
    "forms": ["Non-Collusion Affidavit", "Vendor Information Form"],
    "addenda": [
        {
            "num": 1,
            "date": "2025-01-15",
            "notes": "Clarifications from pre-bid meeting.",
            "url": "https://example.com/addendum1.pdf"
        }
    ],
    "events": [
        {
            "type": "Pre-Bid Meeting",
            "iso": "2025-01-20T10:00:00-08:00",
            "location": "City Hall, Room 201",
            "notes": "Mandatory attendance required"
        }
    ],
    "pw": True,
    "ld": False
}

# Run the normalizer
normalized = normalize_planetbids(sample_raw)

# Print the structured output
import json
print(json.dumps(normalized.to_json(), indent=2))
