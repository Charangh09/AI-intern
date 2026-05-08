# Financial Document Analyzer

![License](https://img.shields.io/github/license/Charangh09/AI-intern)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Issues](https://img.shields.io/github/issues/Charangh09/AI-intern)
![CI](https://img.shields.io/github/actions/workflow/status/Charangh09/AI-intern/ci.yml?branch=main)

Financial Document Analyzer is a focused FastAPI service that analyzes financial PDF documents using a multi-agent AI pipeline. Outputs are evidence-based, strictly grounded in the uploaded PDF, and returned as structured JSON for downstream consumption.

✨ Key goals: accuracy, traceability, and production readiness.

----

## Highlights

- Evidence-first analysis: nothing is inferred beyond the document.
- Multi-agent pipeline orchestrated by CrewAI for separation of concerns.
- Uses LangChain `PyPDFLoader` for robust PDF ingestion.
- Clean JSON output saved in `outputs/` and temporary files removed.

## Architecture & Workflow

1. Client uploads a financial PDF to `POST /analyze`.
2. File is stored temporarily in `data/`.
3. CrewAI runs four agents sequentially:
   - Verifier Agent — validate PDF and extract facts.
   - Financial Analyst Agent — revenue, profitability, cash flow analysis.
   - Risk Assessor Agent — identify stated financial risks.
   - Investment Advisor Agent — synthesize a balanced investment insight.
4. System returns structured JSON and stores the output in `outputs/`.
5. Temporary files are deleted.

Required output keys

- `revenue_analysis`
- `profitability_analysis`
- `cash_flow_analysis`
- `risk_assessment`
- `investment_insight`

----

## Tech Stack

| Layer | Technology |
|---|---|
| API | FastAPI |
| Orchestration | CrewAI |
| LLM | OpenAI GPT-4o-mini |
| PDF Loading | LangChain PyPDFLoader |
| Vector DB (optional) | chromadb |
| Config | python-dotenv |
| Server | uvicorn |

----

## Folder structure (professional view)

```
Financial Document Analyzer/
├─ agents.py            # CrewAI agent definitions
├─ main.py              # FastAPI app and routes
├─ task.py              # orchestration helpers
├─ tools.py             # file handling & utilities
├─ requirements.txt     # runtime dependencies
├─ data/                # temporary uploads (cleaned automatically)
├─ outputs/             # generated JSON analyses
└─ README.md
```

----

## Installation & Setup

Clone, create a venv, and install:

```bash
git clone https://github.com/Charangh09/AI-intern.git
cd AI-intern
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` containing at least:

```env
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini
# Optional: CHROMADB settings, CREWAI_TOKEN
```

Run the app locally:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

----

## API Reference

### POST /analyze

Accepts a single PDF upload, runs the agent pipeline, and returns a validated JSON analysis.

- Content-Type: `multipart/form-data`
- Form field: `file` — PDF file (required)

Example request (cURL):

```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Accept: application/json" \
  -F "file=@/path/to/report.pdf"
```

Example successful response:

```json
{
  "revenue_analysis": "Carefully cited revenue observations from the document...",
  "profitability_analysis": "Profitability notes grounded in table X and section Y...",
  "cash_flow_analysis": "Cash flow commentary based on statement on page N...",
  "risk_assessment": "Enumerated risks as directly stated in the PDF...",
  "investment_insight": "A balanced, evidence-based insight anchored to the report."
}
```

Notes

- The analysis must be traceable to the source document. The pipeline is designed to refuse or return partial failure if required evidence is missing.

----

## Security & Operational Notes

- Keep `OPENAI_API_KEY` and other secrets out of source control — use environment variables or a secrets manager.
- Enforce upload size limits and file-type checks.
- Parse PDFs in a sandbox when possible and validate parsed content before passing to the model.
- Log minimal personal data; treat outputs as potentially sensitive and restrict access.

----

## Deployment

Minimal production guidance:

- Containerize the app and run behind a TLS-terminating reverse proxy (NGINX/ALB).
- Use a process manager (Gunicorn + Uvicorn workers or systemd) and autoscaling as needed.
- Store outputs in a secure store and rotate logs. Use a secret manager for API keys.

Example Dockerfile snippet

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

----

## Future Improvements

- Add a non-blocking worker queue for large documents.
- Add E2E tests for the agent pipeline and JSON schema validation.
- Optional vectorized retrieval when processing very large reports.
- Role-based access control and audit logs for sensitive deployments.

----

## Contributing

Contributions are welcome. Please:

1. Fork the repo and open a feature branch.
2. Keep PRs small and scoped.
3. Add tests where applicable and document behavior changes.
4. Use descriptive commit messages and reference related issues.

----

## License

This project is available under the MIT License. Add a `LICENSE` file to the repository root to make this explicit.

----

If you'd like, I can also:

- add a `LICENSE` file (MIT),
- create a `Dockerfile` and `docker-compose.yml`,
- add a small GitHub Actions workflow for linting and tests.

File: [README.md](README.md)
