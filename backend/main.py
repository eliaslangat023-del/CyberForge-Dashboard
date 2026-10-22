from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import nmap_scan, bettercap, beeftools

app = FastAPI(title="Security Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # match Vite port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nmap_scan.router, prefix="/nmap", tags=["Nmap"])
app.include_router(bettercap.router, prefix="/bettercap", tags=["Bettercap"])
app.include_router(beeftools.router, prefix="/beef", tags=["BeEF"])

