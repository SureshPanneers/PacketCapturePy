# Network Packet Analysis & Protocol Classification

This repository contains a **Python FastAPI microservice** (backend) and a **React** dashboard (frontend) for network packet capture, parsing, simple classification, and visualization. The backend supports a **mock** capture mode (no root privileges or libpcap required) and a **real** capture mode using `scapy` when available.

---
## What's included
- `backend/` — FastAPI service with packet capture (mock + optional scapy), parsers, simple classifier, and API endpoints.
- `frontend/` — React dashboard (simple, single-page) to visualize protocol breakdown, packet list, filters and upload PCAP.
- `docker-compose.yml` — run both services with Docker (optional).
- `tests/` — pytest unit tests for parser & classifier.
- `run_in_pycharm.md` — step-by-step instructions to run the project in PyCharm.

---
## Quick start (recommended for first run - using mock mode)

0. **Clone or download** this repo and unzip.

1. Backend (Python 3.9+ recommended)
```bash
cd backend
python -m venv .venv
source .venv/bin/activate      # or .venv\\Scripts\\activate on Windows (PowerShell)
pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
Backend will start at `http://localhost:8000`

2. Frontend (Node.js, npm)
```bash
cd frontend
npm install
npm start
```
Frontend will start at `http://localhost:3000` and talk to the backend. By default the frontend expects the backend at `http://localhost:8000` (see `frontend/.env` and `frontend/package.json` to change).

3. Use the dashboard to start a **mock capture**, view protocol stats, filter packets, or upload a `.pcap` file (if you have one).

---
## Using real packet capture (optional)
Real capture requires `scapy` and usually root permissions (or set capabilities on the Python binary). To enable real capture:
- Install `scapy` in the backend `.venv` (it is included in `requirements.txt` but might need system packages on Linux).
- Run backend with an environment variable: `USE_REAL_CAPTURE=1 uvicorn app.main:app ...`
- You may need to run as root or give capture capabilities (Linux): `sudo setcap cap_net_raw,cap_net_admin=eip $(which python3)`

If `scapy` is not present or running without privileges, the service will automatically fall back to **mock** mode (safe for testing).

---
## Run with Docker Compose
Requires Docker and docker-compose.
```bash
docker-compose up --build
```
This builds and runs both services. Frontend is served by the Node dev server and proxies API calls to the backend.

---
## PyCharm instructions
Detailed, step-by-step PyCharm guide is provided in `run_in_pycharm.md`.

---
## Notes & limitations
- The classifier included is a **simple heuristic + small synthetic ML training stub** for demonstration. For production, replace with a trained model and more robust parsing.
- Live capture with scapy may need privileges and OS-level dependencies.
