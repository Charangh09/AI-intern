Financial Document Analyzer
Overview
An AI-powered financial analysis system that processes financial PDF reports and generates structured insights using a multi-agent AI pipeline. The project is built using FastAPI, CrewAI, OpenAI GPT models, and LangChain-based PDF processing.
The system follows an evidence-based approach where all generated insights are strictly derived from the uploaded financial document without speculation, external sources, or hallucinated information.

Features


Financial PDF upload and analysis


Multi-agent AI workflow using CrewAI


Revenue, profitability, and cash flow analysis


Financial risk assessment


Evidence-grounded investment insights


Structured JSON output generation


UUID-based analysis tracking


Temporary file storage and automatic cleanup


Robust API validation and error handling



Multi-Agent Pipeline
Verifier Agent


Validates PDF readability


Extracts factual financial information


Ensures document-grounded outputs


Financial Analyst Agent


Analyzes revenue trends


Evaluates profitability metrics


Reviews cash flow performance


Risk Assessor Agent


Identifies financial and operational risks


Detects liquidity concerns and disclosures


Investment Advisor Agent


Combines insights from all agents


Generates balanced investment analysis


Produces final structured JSON response



Workflow
PDF Upload → FastAPI Endpoint → PDF Extraction → CrewAI Agent Pipeline → JSON Validation → Structured Financial Analysis

API Endpoints
MethodEndpointDescriptionGET/Health check endpointPOST/analyzeUpload PDF and generate analysis

Output Structure
{  "revenue_analysis": "",  "profitability_analysis": "",  "cash_flow_analysis": "",  "risk_assessment": "",  "investment_insight": ""}

Tech Stack
TechnologyPurposeFastAPIBackend API FrameworkCrewAIMulti-Agent OrchestrationOpenAI GPT-4o-miniFinancial Reasoning & AnalysisLangChain PyPDFLoaderPDF Text ExtractionUvicornAPI ServerChromaDBVector Storage Supportpython-dotenvEnvironment Configuration

Security & Reliability


Accepts only .pdf files


Environment-based API key management


Temporary file cleanup after processing


Structured JSON schema validation


Evidence-only prompting to minimize hallucination



Key Achievements


Developed a scalable AI-powered financial analysis backend


Designed a modular 4-agent financial intelligence pipeline


Implemented document-grounded AI analysis workflows


Automated extraction and interpretation of financial reports


Built production-ready REST APIs with structured outputs

