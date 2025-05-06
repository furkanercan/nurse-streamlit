# NurseGame RAG UI

This is a simple Streamlit-based UI for testing a Retrieval-Augmented Generation (RAG) chatbot for the NurseGame project.

## Features

- Select patient (1 to 8)
- Chat with embedded Q&A data per patient
- Works with a FastAPI backend deployed on Render

## Run Locally

1. Clone the repo
2. Create a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
