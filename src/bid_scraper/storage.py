import os, json, re
from datetime import datetime
from typing import Dict, Any

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "opportunities")

def _safe(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")

def save_opportunity(opp_json: Dict[str, Any]) -> str:
    os.makedirs(DATA_DIR, exist_ok=True)
    number = opp_json.get("solicitation_number") or "NO-NUM"
    title  = opp_json.get("project_title") or "untitled"
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    fname = f"{_safe(number)}__{_safe(title)[:50]}__{ts}.json"
    path = os.path.join(DATA_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(opp_json, f, ensure_ascii=False, indent=2)
    return path
