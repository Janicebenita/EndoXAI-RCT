@echo off
cd /d "%~dp0"
echo Starting EndoXAI clean model-backed server...
echo Open http://localhost:8080 in your browser.
py -m uvicorn fastapi_app:app --host 0.0.0.0 --port 8080
pause
