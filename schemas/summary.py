from pydantic import BaseModel
from enum import Enum
from typing import List, Optional


class RiskLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TenantSummary(BaseModel):
    tenant_name: str
    risk_level: RiskLevel  # Enum with values: LOW, MEDIUM, HIGH
    payments_behavior: str
    issues_pending: List[str]
    overall_score: str
    recommended_action: str
