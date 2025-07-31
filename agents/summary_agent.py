import json
import os
from typing import Optional
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI

from schemas.tenant import Tenant
from schemas.summary import TenantSummary

load_dotenv()

with open("prompts/summarize_tenants.txt") as f:
    prompt_text = f.read()

parser = PydanticOutputParser(pydantic_object=TenantSummary)

prompt = PromptTemplate(
    template=prompt_text,
    input_variables=["tenant_data"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

llm = ChatOpenAI(model="gpt-4", temperature=0.3, api_key=os.getenv("OPENAI_API_KEY"))

chain = prompt | llm | parser


def summarize_tenant(tenant: Tenant) -> Optional[TenantSummary]:
    try:
        input_data = json.dumps(tenant.model_dump(), indent=2, default=str)
        result = chain.invoke({"tenant_data": input_data})
        return result
    except Exception as e:
        print("❌ Error while parsing output:")
        print(e)
        return None
