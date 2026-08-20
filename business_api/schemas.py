from pydantic import BaseModel
from typing import Optional


class InquiryCreate(BaseModel):
    customer_name: str
    phone: str
    event_type: str
    event_date: str
    guest_count: int
    preferred_hall: Optional[str] = None
    message: Optional[str] = None


class AppointmentCreate(BaseModel):
    customer_name: str
    phone: str
    staff_id: str
    date: str
    time: str
    purpose: str