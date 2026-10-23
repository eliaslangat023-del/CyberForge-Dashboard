# CyberForge Dashboard

A local React + FastAPI dashboard for authorized security labs, integrating Nmap and optional Bettercap/BeEF tooling.

## Use responsibly
Run scans and security tools only against systems you own or have explicit permission to test. Keep this dashboard bound to localhost during development. Do not expose privileged tooling endpoints directly to the public internet.

## Requirements
- Python 3.10+
- Node.js and npm
- Nmap
- Backend packages from `backend/requirements.txt`
- Frontend packages from `frontend/package.json`
- Bettercap/BeEF only if you intentionally configure those integrations

## Start the backend
From the repository root, create and activate a virtual environment, install backend dependencies, then run the app using the import path that matches your folder layout. For a root-level `backend/` package:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

If running from inside `backend/`, use `uvicorn main:app --host 127.0.0.1 --port 8000` instead. Review the frontend's configured API URL before launching it.

## Security checklist
- Add authentication and per-action authorization before using beyond a single-user local lab.
- Validate and allowlist target hosts, ports, and command arguments server-side; never pass unsanitized user input to shell commands.
- Keep CORS limited to the exact local frontend origin.
- Store API tokens in environment variables; never put live tokens in source control or README examples.
- Run subprocesses with least privilege, timeouts, and bounded output; do not run the web server as root.
- Do not commit scan output, target inventories, credentials, or session data.

## Development
Run linting/tests where configured and verify the complete diff before merging. This repository is a learning project; integrations may require local setup and have not been represented as production-ready.
