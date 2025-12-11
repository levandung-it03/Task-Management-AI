# Reinstall `.venv`
> cd D:\project

> py -3.12 -m venv .venv

> .\.venv\Scripts\activate

> pip install fastapi uvicorn[standard]

# To run
> uvicorn app.main:app --host 0.0.0.0 --port 8000 --timeout-keep-alive 60