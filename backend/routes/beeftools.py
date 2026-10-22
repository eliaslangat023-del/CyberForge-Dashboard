from fastapi import APIRouter

router = APIRouter()

@router.get("/hook")
async def deliver_hook():
    return {"payload": "<script src='http://127.0.0.1:3000/hook.js'></script>"}
