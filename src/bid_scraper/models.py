from dataclasses import dataclass, field
from typing import List, Dict, Any
from datetime import datetime
import pytz


@dataclass
class MandatoryEvent:
    type: str
    date_time_local: str
    location: str = ""
    notes: str = ""


@dataclass
class Addendum:
    number: str
    date: str = ""
    notes: str = ""
    url: str = ""


@dataclass
class Opportunity:
    issuing_agency: str = ""
    project_title: str = ""
    solicitation_number: str = ""
    solicitation_type: str = ""
    due_date_local: str = ""
    timezone: str = ""
    submission_method: str = ""
    mandatory_events: List[MandatoryEvent] = field(default_factory=list)
    addenda: List[Addendum] = field(default_factory=list)
    required_documents: List[str] = field(default_factory=list)
    forms: List[str] = field(default_factory=list)
    insurance_bonding: str = ""
    scope_summary: str = ""
    product_categories: List[str] = field(default_factory=list)
    delivery_installation: str = ""
    contacts: List[Dict[str, str]] = field(default_factory=list)
    submission_portal_links: List[str] = field(default_factory=list)
    questions_due: str = ""
    budget_or_estimate: str = ""
    prevailing_wage: str = "unknown"
    liquidated_damages: str = "unknown"
    other_compliance: List[str] = field(default_factory=list)
    unknowns: List[str] = field(default_factory=list)

    def to_json(self) -> Dict[str, Any]:
        return {
            **self.__dict__,
            "mandatory_events": [me.__dict__ for me in self.mandatory_events],
            "addenda": [ad.__dict__ for ad in self.addenda],
        }


def iso_local(dt: datetime, tz_name: str) -> str:
    """Convert naive or UTC datetime to ISO8601 with timezone awareness."""
    tz = pytz.timezone(tz_name)
    return tz.normalize(dt.astimezone(tz)).isoformat()
