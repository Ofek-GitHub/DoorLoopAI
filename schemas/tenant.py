# schemas/tenant.py

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date
from enum import Enum


class RentStatus(str, Enum):
    paid = "paid"
    late = "late"
    unpaid = "unpaid"


class Tenant(BaseModel):
    name: str
    unit: str
    rent_status: RentStatus  # 👈 Enum replaces string
    last_payment_date: date
    maintenance_issues: List[str]
    notes: Optional[str] = None
    lease_end_date: Optional[date] = None
    contact_info: Optional[EmailStr] = None
