from typing import List
from schemas.tenant import Tenant
import json


def load_tenants_from_file(path: str = "data/tenants.json") -> List[Tenant]:
    with open(path, "r") as f:
        raw = json.load(f)
    return [Tenant(**entry) for entry in raw]
