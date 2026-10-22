#!/bin/bash

echo "🔧 Cleaning up old frontend..."
rm -rf frontend

echo "🔧 Ensuring backend structure..."
mkdir -p backend/routes
touch backend/routes/__init__.py

# Fix main.py imports
cat > backend/main.py << 'EOF'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import nmap_scan, bettercap, beeftools

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

echo "✅ Backend fixed. Now setting up frontend..."

# Create React app with --legacy-peer-deps to bypass npm script restrictions
npx create-react-app frontend --use-npm --legacy-peer-deps

echo "✅ Frontend created. Drop your custom components into frontend/src/components/"
echo "👉 Run backend with: uvicorn backend.main:app --reload"
echo "👉 Run frontend with: cd frontend && npm start"
