from crewai import Task

from agents import verifier, financial_analyst, risk_assessor, investment_advisor
from tools import read_financial_document


verification_task = Task(
    description=(
        "Use the tool to read the uploaded PDF at {file_path}. Confirm it is a financial document and "
        "extract concise factual evidence relevant to revenue, profitability, cash flow, and risk. "
        "Only use statements explicitly present in the document text. "
        "Do not use external knowledge, web search, assumptions, or invented data."
    ),
    expected_output=(
        "A concise evidence report with: (1) document validation status, (2) key factual excerpts, "
        "(3) page references if available, and (4) any data limitations found in the document."
    ),
    agent=verifier,
    tools=[read_financial_document],
    async_execution=False,
)


financial_analysis_task = Task(
    description=(
        "Using the verified evidence from the prior task, produce three sections: revenue analysis, "
        "profitability analysis, and cash flow analysis. "
        "Every claim must be directly supported by the uploaded document at {file_path}. "
        "If data is missing, explicitly state that it is not present."
    ),
    expected_output=(
        "A structured analysis with exactly these sections: revenue_analysis, profitability_analysis, "
        "cash_flow_analysis. No speculation and no external references."
    ),
    agent=financial_analyst,
    tools=[read_financial_document],
    context=[verification_task],
    async_execution=False,
)


risk_assessment_task = Task(
    description=(
        "Based on verified evidence and financial analysis, produce a conservative risk assessment using only "
        "facts present in the uploaded PDF at {file_path}. "
        "Do not infer risks without textual support."
    ),
    expected_output=(
        "A single section named risk_assessment with evidence-based risk observations and explicit limitations."
    ),
    agent=risk_assessor,
    tools=[read_financial_document],
    context=[verification_task, financial_analysis_task],
    async_execution=False,
)


investment_insight_task = Task(
    description=(
        "Produce the final result as strict JSON with keys: revenue_analysis, profitability_analysis, "
        "cash_flow_analysis, risk_assessment, investment_insight. "
        "The investment_insight value must be balanced and non-speculative. "
        "Use only prior task outputs grounded in {file_path}. "
        "Do not add markdown, code fences, or extra keys."
    ),
    expected_output=(
        '{"revenue_analysis":"...","profitability_analysis":"...","cash_flow_analysis":"...",'
        '"risk_assessment":"...","investment_insight":"balanced and non-speculative"}'
    ),
    agent=investment_advisor,
    context=[verification_task, financial_analysis_task, risk_assessment_task],
    async_execution=False,
)


ALL_TASKS = [
    verification_task,
    financial_analysis_task,
    risk_assessment_task,
    investment_insight_task,
]
