# Financial Document Analyzer

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange)
![License](https://img.shields.io/badge/License-MIT-green)

An AI-powered financial document analysis system that turns financial PDF reports into structured, decision-ready insights.

Financial Document Analyzer uses a multi-agent workflow to validate uploaded reports, extract key financial signals, and return a clean JSON summary covering revenue, profitability, cash flow, risk, and investment outlook.

## Project Overview

Financial reports can be dense, repetitive, and difficult to review quickly. This project provides a focused FastAPI service that helps automate the first layer of financial document analysis while keeping the output structured and easy to consume.

The system is designed around a simple idea: upload a PDF, let specialized AI agents review it from different angles, and receive a concise financial insight report that can support faster review and decision-making.

## Features

- PDF-based financial report analysis
- Multi-agent workflow powered by CrewAI
- Structured JSON output for easy downstream use
- Revenue, profitability, cash flow, risk, and investment insight coverage
- Automatic temporary file cleanup after processing
- Environment-based configuration for safer secret handling
- Lightweight FastAPI backend suitable for demos, prototypes, and extensions

## Workflow

1. A user uploads a financial PDF report.
2. The file is validated and prepared for processing.
3. The document is read using LangChain `PyPDFLoader`.
4. Four AI agents analyze the report from separate financial perspectives.
5. The system returns structured JSON insights.
6. Temporary files are cleaned automatically.

## Multi-Agent Pipeline

The analysis is handled by four specialized agents:

| Agent | Role |
| --- | --- |
| Verifier Agent | Checks whether the uploaded document is valid and suitable for analysis. |
| Financial Analyst Agent | Reviews revenue, profitability, and cash flow signals. |
| Risk Assessor Agent | Identifies financial, operational, or market-related risks mentioned in the report. |
| Investment Advisor Agent | Produces a balanced investment-oriented summary based on the extracted insights. |

### Output Includes

- Revenue analysis
- Profitability analysis
- Cash flow analysis
- Risk assessment
- Investment insight

## Tech Stack

| Technology | Purpose |
| --- | --- |
| FastAPI | Backend API framework |
| CrewAI | Multi-agent orchestration |
| OpenAI GPT-4o-mini | Language model for financial reasoning |
| LangChain PyPDFLoader | PDF parsing and document loading |
| Uvicorn | ASGI server |
| ChromaDB | Vector storage support |
| python-dotenv | Environment variable management |

## Security & Reliability

- API keys and sensitive configuration are managed through environment variables.
- Uploaded files are treated as temporary data and removed after processing.
- PDF validation helps reduce unsupported or invalid file handling.
- Structured JSON responses make the output easier to validate, store, and integrate.
- The architecture keeps each agent focused, making the pipeline easier to debug and extend.

## Future Improvements

- Add background job processing for larger PDFs
- Introduce stronger JSON schema validation
- Add document-level citations for better traceability
- Store analysis history with user-level access controls
- Improve evaluation with sample financial reports and benchmark outputs
- Add a simple dashboard for reviewing generated insights

## License

This project is released under the MIT License.
