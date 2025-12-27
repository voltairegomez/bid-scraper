from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

def score(opp):
    score = 50
    reasons = []
    title = (opp.get("project_title") or "").lower()
    summary = (opp.get("scope_summary") or "").lower()
    text = f"{title} {summary}"

    if any(k in text for k in ["furniture", "casework", "desk", "chair", "workstation"]):
        score += 25; reasons.append("Strong product fit (furniture keywords).")
    if opp.get("prevailing_wage") == "yes":
        score -= 5; reasons.append("Prevailing wage installation risk.")
    if opp.get("liquidated_damages") == "yes":
        score -= 10; reasons.append("Liquidated damages present.")
    if opp.get("required_documents"):
        score += 5; reasons.append("Clear document list provided.")
    if not opp.get("due_date_local"):
        score -= 10; reasons.append("Missing due date.")

    score = max(0, min(100, score))
    if not reasons: reasons.append("Baseline score with limited info.")
    return score, reasons

def checklist(opp):
    docs = opp.get("required_documents", [])
    out = [{"label": d, "filename_hint": d} for d in docs]
    out += [
        {"label": "Completed price sheet", "filename_hint": "Price_Sheet.xlsx"},
        {"label": "Signed proposal PDF", "filename_hint": "Proposal_PureDesignWerx.pdf"},
        {"label": "Non-Collusion Affidavit (if applicable)", "filename_hint": "Non-Collusion.pdf"},
        {"label": "COI meeting insurance limits (if required)", "filename_hint": "COI.pdf"},
    ]
    return out

@app.post("/api/opportunities")
async def receive(req: Request):
    payload = await req.json()
    s, reasons = score(payload)
    return {
        "status": "ok",
        "analysis": {
            "score": s,
            "reasons": reasons,
            "go_no_go": "go" if s >= 70 else "hold",
            "next_actions": [
                "Confirm spec brand equals PDW catalog or equals.",
                "Check delivery: inside delivery / liftgate / union rules.",
                "Confirm insurance & bonding requirements."
            ],
            "submission_checklist": checklist(payload)
        },
        "echo": payload
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
