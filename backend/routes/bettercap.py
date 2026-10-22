from fastapi import APIRouter, WebSocket
import subprocess, asyncio

router = APIRouter()

@router.post("/mitm")
async def start_mitm(iface: str = "wlan0"):
    subprocess.Popen(["bettercap", "-iface", iface])
    return {"status": "ok", "message": f"Bettercap MITM started on {iface}"}

@router.post("/stop")
async def stop_mitm():
    subprocess.Popen(["pkill", "-f", "bettercap"])
    return {"status": "ok", "message": "Bettercap stopped"}

@router.post("/dns_spoof")
async def dns_spoof():
    subprocess.Popen(["bettercap", "-iface", "wlan0", "-eval", "dns.spoof on"])
    return {"status": "ok", "message": "DNS spoofing started"}

@router.post("/arp_spoof")
async def arp_spoof():
    subprocess.Popen(["bettercap", "-iface", "wlan0", "-eval", "arp.spoof on"])
    return {"status": "ok", "message": "ARP spoofing started"}

@router.websocket("/ws")
async def bettercap_logs(ws: WebSocket):
    await ws.accept()
    process = await asyncio.create_subprocess_exec(
        "bettercap", "-iface", "wlan0",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT
    )
    while True:
        line = await process.stdout.readline()
        if not line:
            break
        await ws.send_text(line.decode())
    await ws.close()
