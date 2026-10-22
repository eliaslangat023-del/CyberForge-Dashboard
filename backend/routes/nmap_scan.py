from fastapi import APIRouter, HTTPException
import subprocess
import json

router = APIRouter()

@router.get("/{target}")
async def run_nmap(target: str):
    try:
        # Run nmap with JSON output (-oJ requires nmap >= 7.93)
        result = subprocess.run(
            ["nmap", "-sV", "-oJ", "-", target],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=result.stderr)

        # Parse JSON output from nmap
        try:
            parsed = json.loads(result.stdout)
        except json.JSONDecodeError:
            # fallback: return raw text if JSON parsing fails
            parsed = {"raw_output": result.stdout}

        return {
            "status": "ok",
            "target": target,
            "scan": parsed,
            "timestamp": subprocess.getoutput("date")  # adds run timestamp
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
