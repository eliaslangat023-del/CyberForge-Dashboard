#!/bin/bash

echo "🔧 Resetting backend imports..."
mkdir -p backend/routes
touch backend/routes/__init__.py

cat > backend/main.py << 'EOF'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import backend.routes.nmap_scan as nmap_scan
import backend.routes.bettercap as bettercap
import backend.routes.beeftools as beeftools

app = FastAPI(title="Security Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nmap_scan.router, prefix="/nmap", tags=["Nmap"])
app.include_router(bettercap.router, prefix="/bettercap", tags=["Bettercap"])
app.include_router(beeftools.router, prefix="/beef", tags=["BeEF"])
EOF

echo "✅ Backend imports fixed."

echo "🔧 Resetting frontend..."
rm -rf frontend
mkdir frontend
cd frontend

# Use Vite instead of CRA to bypass npm script restrictions
npm create vite@latest . -- --template react
npm install

echo "✅ Frontend created with Vite (React)."
echo "👉 Run backend: uvicorn backend.main:app --reload"
echo "👉 Run frontend: cd frontend && npm run dev"
