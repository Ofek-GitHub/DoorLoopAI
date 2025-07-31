# main.py

from core.load_data import load_tenants_from_file
from agents.summary_agent import summarize_tenant
from typing import Optional


def main():
    tenants = load_tenants_from_file("data/tenants.json")

    for tenant in tenants:
        print("=" * 50)
        print(f"🧑‍💼 Tenant: {tenant.name}")
        summary = summarize_tenant(tenant)
        if summary is None:
            print("FailedOPS")
        else:
            print(summary.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
