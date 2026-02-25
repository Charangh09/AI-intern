# Financial Document Analyzer

A FastAPI service that takes a financial PDF and extracts structured analysis using a CrewAI agent pipeline. The key constraint: everything comes from the document itself—no speculation, no external data, no guessing.

You upload a PDF, the API runs it through four specialized agents, and you get back clean JSON with revenue, profitability, cash flow, and risk analysis.

## How it works

The flow is straightforward:

1. POST a PDF to `/analyze`
2. The file lands temporarily in `data/`
3. Four agents run in sequence, each doing one thing well
4. Results get validated and saved to `outputs/` with a UUID
5. Temp file gets cleaned up

Each agent has a focused job:

- **Verifier** reads the PDF, flags if it's valid, pulls out raw facts
- **Financial Analyst** digs into the numbers—revenue, profit margins, cash position
- **Risk Assessor** identifies the financial risks that the document actually mentions
- **Investment Advisor** synthesizes everything into a balanced summary, strictly in JSON

All four agents ground their output in what's actually in the PDF. If something isn't there, it doesn't make it into the output.

## Getting started

### Requirements

- Python 3.10, 3.11, or 3.12
- pip

### Setup

Create a virtual environment and activate it:

```bash
# Windows PowerShell
py -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
```

`OPENAI_API_KEY` is required. `OPENAI_MODEL` defaults to `gpt-4o-mini` if not set.

## Running the API

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be at `http://localhost:8000`.

## API

### GET `/`

Health check—confirms the API is running.

Response:
```json
{
  "message": "Financial Document Analyzer API is running"
}
```

### POST `/analyze`

Upload a financial PDF and get back structured analysis.

- Content type: `multipart/form-data`
- `file` (required, `.pdf`): The financial document
- `query` (optional, string): Custom instruction to guide the analysis

Example:

```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@data/TSLA-Q2-2025-Update.pdf" \
  -F "query=Analyze revenue, profitability, cash flow, and risks using only document evidence"
```

Response on success:
```json
{
  "status": "success",
  "output_file": "outputs/analysis_2f1e5f8e-0f3f-46b9-a24f-1fe6a5316e7d.json",
  "analysis": {
    "revenue_analysis": "...",
    "profitability_analysis": "...",
    "cash_flow_analysis": "...",
    "risk_assessment": "...",
    "investment_insight": "balanced and non-speculative"
  }
}
```

The full analysis is saved to the `output_file` path.

## Design decisions

### Evidence-only constraints

The agents are explicitly prompted to source everything from the PDF. No web lookups, no external data, no "best practice" interpolation. If margin data isn't in the doc, it doesn't get reported. This keeps the output honest and verifiable.

### Temporary file cleanup

PDFs get stored temporarily in `data/` while they're being processed, then deleted afterward. Nothing persists except the JSON output in `outputs/`.

### JSON validation

The final response from the investment advisor is validated against the expected schema before being returned. If it doesn't match, the request fails rather than returning partial or malformed data.

## Security

- Only `.pdf` files are accepted
- Temporary files are cleaned up after processing
- No web requests or external API calls to source claims
- API keys are loaded from environment variables, not hardcoded
- Prompts are designed to prevent hallucination and speculation

For production, you'll want to add:

- Authentication and rate limiting
- Upload size limits at the gateway level
- Structured logging and monitoring
- HTTPS with proper secret management
- Input sanitization for the optional `query` parameter

## Tech stack

- **API:** FastAPI with Uvicorn
- **Agent orchestration:** CrewAI (0.130.0)
- **PDF handling:** LangChain Community PyPDFLoader and pypdf
- **Model:** OpenAI SDK
- **Config:** python-dotenv

## Contributing

If you want to contribute:

1. Create a branch off `main`
2. Keep changes focused
3. Don't break the `/analyze` response contract
4. Add tests for behavior changes
5. Open a PR with a short summary and steps to verify

## License

Add a `LICENSE` file (MIT, Apache-2.0, etc.) and update this section.
