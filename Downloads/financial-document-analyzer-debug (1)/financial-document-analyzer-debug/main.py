import json
import os
import uuid
from datetime import datetime

from fastapi import FastAPI, File, Form, HTTPException, UploadFile

from crewai import Crew, Process

from agents import verifier, financial_analyst, risk_assessor, investment_advisor
from task import ALL_TASKS


app = FastAPI(title="Financial Document Analyzer", version="1.0.0")


REQUIRED_KEYS = {
    "revenue_analysis",
    "profitability_analysis",
    "cash_flow_analysis",
    "risk_assessment",
    "investment_insight",
}


def _build_crew() -> Crew:
    return Crew(
        agents=[verifier, financial_analyst, risk_assessor, investment_advisor],
        tasks=ALL_TASKS,
        process=Process.sequential,
        verbose=False,
    )


def _parse_json_result(raw_result: object) -> dict:
    text = str(raw_result).strip()

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Crew output is not valid JSON: {exc}") from exc

    if not isinstance(parsed, dict):
        raise ValueError("Crew output must be a JSON object.")

    missing = REQUIRED_KEYS.difference(parsed.keys())
    if missing:
        raise ValueError(f"Crew output is missing required keys: {sorted(missing)}")

    return {
        "revenue_analysis": str(parsed["revenue_analysis"]),
        "profitability_analysis": str(parsed["profitability_analysis"]),
        "cash_flow_analysis": str(parsed["cash_flow_analysis"]),
        "risk_assessment": str(parsed["risk_assessment"]),
        "investment_insight": "balanced and non-speculative",
    }


def run_crew(query: str, file_path: str) -> dict:
    crew = _build_crew()
    raw = crew.kickoff(inputs={"query": query, "file_path": file_path})
    return _parse_json_result(raw)


@app.get("/")
def root() -> dict:
    return {"message": "Financial Document Analyzer API is running"}


@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document using only document evidence."),
) -> dict:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Uploaded file must have a filename.")

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF uploads are supported.")

    os.makedirs("data", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    file_id = str(uuid.uuid4())
    input_path = os.path.join("data", f"upload_{file_id}.pdf")

    try:
        content = await file.read()
        if not content:
            raise HTTPException(status_code=400, detail="Uploaded file is empty.")

        with open(input_path, "wb") as f:
            f.write(content)

        sanitized_query = (query or "").strip() or "Analyze this financial document using only document evidence."

        analysis = run_crew(query=sanitized_query, file_path=input_path)

        output_payload = {
            "file_name": file.filename,
            "file_path": input_path,
            "query": sanitized_query,
            "analysis": analysis,
            "generated_at_utc": datetime.utcnow().isoformat() + "Z",
        }

        output_path = os.path.join("outputs", f"analysis_{file_id}.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_payload, f, ensure_ascii=True, indent=2)

        return {
            "status": "success",
            "output_file": output_path,
            "analysis": analysis,
        }

    except HTTPException:
        raise
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Internal processing error: {exc}") from exc
    finally:
        if os.path.exists(input_path):
            try:
                os.remove(input_path)
            except OSError:
                pass


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
