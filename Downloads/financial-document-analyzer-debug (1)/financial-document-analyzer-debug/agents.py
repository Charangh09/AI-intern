import os
from dotenv import load_dotenv
from crewai import Agent, LLM

from tools import read_financial_document

load_dotenv()


def _build_llm() -> LLM:
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set.")

    return LLM(
        model=model,
        api_key=api_key,
        temperature=0,
    )


llm = _build_llm()


verifier = Agent(
    role="Financial Document Verifier",
    goal=(
        "Validate that the uploaded file at {file_path} is a readable financial PDF and "
        "extract only explicit factual evidence from that document."
    ),
    backstory=(
        "You are a compliance-first document verification specialist. "
        "You never infer missing facts and never use external sources."
    ),
    verbose=False,
    memory=False,
    allow_delegation=False,
    tools=[read_financial_document],
    llm=llm,
)


financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal=(
        "Analyze revenue, profitability, and cash flow using only evidence extracted from "
        "the uploaded financial document."
    ),
    backstory=(
        "You are a rigorous financial analyst focused on verifiable statements from primary documents."
    ),
    verbose=False,
    memory=False,
    allow_delegation=False,
    tools=[read_financial_document],
    llm=llm,
)


risk_assessor = Agent(
    role="Financial Risk Assessor",
    goal=(
        "Identify business and financial risks strictly supported by statements in the uploaded PDF."
    ),
    backstory=(
        "You perform conservative, evidence-based risk assessment without speculation."
    ),
    verbose=False,
    memory=False,
    allow_delegation=False,
    tools=[read_financial_document],
    llm=llm,
)


investment_advisor = Agent(
    role="Investment Insight Advisor",
    goal=(
        "Provide a balanced, non-speculative investment insight based only on documented evidence "
        "from the uploaded PDF and prior team analysis."
    ),
    backstory=(
        "You produce compliance-safe, non-promotional insights and avoid prescriptive trading calls."
    ),
    verbose=False,
    memory=False,
    allow_delegation=False,
    llm=llm,
)
