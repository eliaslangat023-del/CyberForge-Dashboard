from fastapi import APIRouter, HTTPException
import requests
import os

router = APIRouter()

# Store your BeEF API token in an environment variable
BEEF_API_URL = "http://127.0.0.1:3000/api/hooks"
BEEF_API_TOKEN = os.getenv("BEEF_API_TOKEN")  # set this before running uvicorn

@router.get("/beef/clients")
def get_beef_clients():
    try:
        res = requests.get(f"{BEEF_API_URL}?token={BEEF_API_TOKEN}")
        if res.status_code != 200:
            raise HTTPException(status_code=res.status_code, detail="Failed to fetch BeEF clients")
        return res.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
