from models import Opportunity, MandatoryEvent, Addendum

def normalize_planetbids(raw: dict) -> Opportunity:
    """Convert raw PlanetBids JSON data to an Opportunity object."""
    opp = Opportunity()

    opp.issuing_agency = raw.get("agency", "")
    opp.project_title = raw.get("title", "")
    opp.solicitation_number = raw.get("number", "")
    opp.solicitation_type = raw.get("type", "")
    opp.timezone = raw.get("timezone", "America/Los_Angeles")
    opp.due_date_local = raw.get("due_iso", "")
    opp.submission_method = raw.get("submission", "")
    opp.scope_summary = raw.get("summary", "")

    # Required documents and forms
    opp.required_documents = raw.get("required_docs", [])
    opp.forms = raw.get("forms", [])

    # Addenda
    for a in raw.get("addenda", []):
        opp.addenda.append(
            Addendum(
                number=str(a.get("num", "")),
                date=a.get("date", ""),
                notes=a.get("notes", ""),
                url=a.get("url", "")
            )
        )

    # Events (like pre-bid meetings)
    for e in raw.get("events", []):
        opp.mandatory_events.append(
            MandatoryEvent(
                type=e.get("type", ""),
                date_time_local=e.get("iso", ""),
                location=e.get("location", ""),
                notes=e.get("notes", "")
            )
        )

    # Compliance flags
    if raw.get("pw") is True:
        opp.prevailing_wage = "yes"
    elif raw.get("pw") is False:
        opp.prevailing_wage = "no"

    if raw.get("ld") is True:
        opp.liquidated_damages = "yes"
    elif raw.get("ld") is False:
        opp.liquidated_damages = "no"

    # Fill in unknowns
    for key in ("insurance", "bonding"):
        if not raw.get(key):
            opp.unknowns.append(f"Missing {key} requirements")

    return opp
