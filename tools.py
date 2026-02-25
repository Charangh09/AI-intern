import os
from crewai.tools import tool
from langchain_community.document_loaders import PyPDFLoader


@tool("read_financial_document")
def read_financial_document(file_path: str) -> str:
    """Read and return text from a financial PDF file."""
    if not file_path:
        raise ValueError("file_path is required.")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if not file_path.lower().endswith(".pdf"):
        raise ValueError("Only PDF files are supported.")

    loader = PyPDFLoader(file_path)
    pages = loader.load()

    if not pages:
        raise ValueError("The PDF appears to be empty or unreadable.")

    chunks = []
    for idx, page in enumerate(pages, start=1):
        content = (page.page_content or "").strip()
        if content:
            chunks.append(f"[Page {idx}]\n{content}")

    if not chunks:
        raise ValueError("No extractable text was found in the PDF.")

    return "\n\n".join(chunks)
