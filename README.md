Financial Document Analyzer
Financial Document Analyzer is an AI-powered backend application that analyzes financial PDF reports and generates structured financial insights using a multi-agent AI workflow. Built with FastAPI, CrewAI, and OpenAI models, the system focuses on delivering evidence-based analysis where every insight is strictly derived from the uploaded document without speculation or external data.
The application processes uploaded financial documents through a sequential pipeline of specialized AI agents. The Verifier Agent validates the PDF and extracts factual information, the Financial Analyst Agent evaluates revenue, profitability, and cash flow performance, the Risk Assessor identifies financial risks mentioned in the report, and the Investment Advisor combines all findings into a structured JSON response.
The API supports PDF uploads through REST endpoints, temporary file handling, UUID-based tracking, JSON validation, and automated cleanup after processing. The final output includes detailed revenue analysis, profitability insights, cash flow evaluation, risk assessment, and investment recommendations generated entirely from document evidence.
Key Highlights


Built a multi-agent AI pipeline using CrewAI with 4 specialized financial analysis agents


Developed scalable REST APIs using FastAPI and Uvicorn


Integrated OpenAI GPT models for document-grounded financial reasoning


Implemented PDF extraction using LangChain PyPDFLoader


Designed evidence-only prompting to reduce hallucination and speculative outputs


Added structured JSON validation and error handling mechanisms


Implemented secure temporary file management and cleanup workflows


Generated machine-readable financial insights for automation and analytics use cases


Tech Stack


Backend: FastAPI


AI Orchestration: CrewAI


LLM: OpenAI GPT-4o-mini


PDF Processing: LangChain PyPDFLoader


Server: Uvicorn


Database/Storage: ChromaDB


Environment Management: python-dotenv

