from pydantic import BaseModel, Field
from typing import Optional, List

class Opportunity(BaseModel):
    portal: str
    external_id: str = Field(..., description="Solicitation number or stable ID")
    title: str
    agency: Optional[str] = None
    url: str
    type: Optional[str] = None
    due_date: Optional[str] = None
    timezone: Optional[str] = None
    status: Optional[str] = None
    categories: List[str] = []
    city: Optional[str] = None
    state: Optional[str] = None
    posted_date: Optional[str] = None
    close_date: Optional[str] = None


