# ⚡ CyberForge Dashboard

// Welcome, traveler. You’ve stumbled into CyberForge — a stitched‑together hacker cockpit built with React + FastAPI.
// It’s not a corporate dashboard. It’s a Frankenstein mash‑up of Nmap, Bettercap, and BeEF, duct‑taped into one GUI.
// ⚠️ Lab use only. Unauthorized use = bad karma + orange jumpsuit.

---

## 🕹️ Features
// What this beast can actually do (besides look cool):

- Nmap panel — JSON scans without squinting at raw terminal output.
- Bettercap integration — MITM monitoring and injection workflows.
- BeEF hook monitor — track browsers that wander into your trap.
- React frontend — modular panels, nerd‑approved.
- FastAPI backend — proxies secrets, keeps your repo clean.

---

## 🛠️ Requirements
// Stuff you need installed before pressing shiny buttons:

- Python ≥3.10
- Node.js + npm
- FastAPI + Uvicorn
- Nmap ≥7.93 (JSON output support)
- Bettercap ≥2.41
- BeEF (`apt install beef-xss` on Kali)
- Ruby gems if running BeEF manually (`msgpack`, `thin`, `em-websocket`, `rack`)

---

## 🚀 Setup
// How to summon the dashboard without sacrificing goats:

### Backend
```bash
cd backend
pip install -r requirements.txt

Start BeEF:
bash

sudo beef-xss-start

Grab the API token (BeEF prints it at startup or via /api/admin/login). Then export it:
bash

export BEEF_API_TOKEN=<your_token_here>
sudo uvicorn backend.main:app --reload

Frontend
bash

cd frontend
npm install
npm start

Dashboard runs at:
Code

http://localhost:3000

🧪 BeEF Integration (Browser BBQ)

// This is where browsers get skewered. Only in your lab. Don’t be “that guy.”
Getting the Token

BeEF is moody — it generates a new API token every time it wakes up. Options:

    Run sudo ./beef in /usr/share/beef-xss if you’ve appeased the Ruby gem gods.

    Or set admin creds in config.yaml, log in at http://127.0.0.1:3000/ui/panel, then curl /api/admin/login to fetch the token.

Using the Token

Export it before running FastAPI:
bash

export BEEF_API_TOKEN=deadbeefcafebabe1234567890abcdef

Now your dashboard’s BeEF button will actually show hooked clients instead of shrugging with a 200 OK.
📦 requirements.txt (backend)

// Python dependencies, because pip loves lists:
Code

fastapi
uvicorn
requests
python-dotenv

🖼️ Workflow Diagram (ASCII edition)

// Because ASCII art is still cooler than PowerPoint:
Code

[ React Dashboard ] ---> [ FastAPI Proxy ] ---> [ BeEF / Nmap / Bettercap ]
        |                        |                        |
        |                        |                        |
        +-----> User clicks ---->+-----> Injects token --->+-----> Tools respond

🧑‍💻 Contributing

// Rules of engagement:

    Fork it, hack it, break it, fix it.

    PRs welcome — especially if you tame BeEF’s gem tantrums.

    Keep commits clean: one feature per commit, no “final_final_fix_really_this_time.js”.

⚠️ Disclaimer

// Legal voodoo: read this or risk the jumpsuit.

This project is for educational and research purposes only. Do not use against unauthorized systems. You are responsible for your own actions. Unauthorized use = bad karma + orange jumpsuit.
