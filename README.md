# Financial Document Analyzer

An AI-powered financial document analysis system that processes financial PDF reports and generates structured insights using a multi-agent AI workflow.

Built with FastAPI, CrewAI, OpenAI GPT models, and LangChain, the project focuses on delivering evidence-based financial analysis where every insight is generated strictly from the uploaded document without speculation or external information.

---

## Features

- AI-powered financial PDF analysis
- Multi-agent workflow using CrewAI
- Revenue, profitability, and cash flow analysis
- Financial risk identification
- Evidence-based investment insights
- Structured JSON output generation
- Temporary file cleanup after processing
- Secure and scalable REST API architecture
- Robust validation and error handling

---

## How It Works

1. User uploads a financial PDF document
2. The document is validated and processed
3. Multiple AI agents analyze different financial aspects
4. Insights are combined into a structured JSON response
5. Results are saved and temporary files are deleted

---

## Multi-Agent Pipeline

### Verifier Agent
- Validates uploaded PDFs
- Extracts factual financial information
- Ensures outputs remain document-grounded

### Financial Analyst Agent
- Analyzes revenue trends
- Evaluates profitability metrics
- Reviews cash flow performance

### Risk Assessor Agent
- Identifies financial and operational risks
- Detects liquidity concerns and disclosures

### Investment Advisor Agent
- Combines all findings
- Generates balanced investment insights
- Produces final structured JSON output

---

## Output Structure

The generated response includes:

- Revenue Analysis
- Profitability Analysis
- Cash Flow Analysis
- Risk Assessment
- Investment Insight

---

## Tech Stack

- FastAPI
- CrewAI
- OpenAI GPT-4o-mini
- LangChain PyPDFLoader
- Uvicorn
- ChromaDB
- python-dotenv

---

## Security & Reliability

- Accepts only PDF files
- Temporary file cleanup after processing
- Environment-based API key management
- Structured JSON validation
- Evidence-only prompting to reduce hallucinations

---

## Future Improvements

- OCR support for scanned PDFs
- Multi-document comparison
- Authentication and rate limiting
- Analytics dashboard
- Docker and cloud deployment
- Monitoring and logging support

---

## License

This project is licensed under the MIT License.

